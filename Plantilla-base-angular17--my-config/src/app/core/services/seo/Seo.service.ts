import { Injectable } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';
import { IMetaTagConfig, IMetaIndex } from '../../models/IMetadata.interface';

@Injectable({
	providedIn: 'root',
})
export class SeoService {
	constructor(
		private readonly _title: Title,
		private readonly _meta: Meta
	) {}

	public setCanonicalURL(url: string): void {
		if (!URL.canParse(url)) throw new Error('Invalid URL');

		this._meta.updateTag({ name: 'canonical', content: url });
	}

	public applyIndexFollow(value: boolean = true): void {
		this._meta.updateTag({
			name: 'robots',
			content: value ? 'index, follow' : 'noindex, nofollow',
		});
	}

	public setTitle(title: string): void {
		this._title.setTitle(title);
	}

	public updateMetaTags({ metaTags, ogTags }: Partial<IMetaTagConfig>): void {
		if (!metaTags && !ogTags) return;

		this.setMetaTags(metaTags);
		this.setMetaTags(ogTags);
	}

	private setMetaTags(objectTags: Partial<IMetaIndex | undefined>): void {
		if (objectTags === undefined || Object.keys(objectTags).length <= 0) return;

		for (const [key, value] of Object.entries(objectTags)) {
			if (value === undefined || value.trim() === '') continue;

			if (key.startsWith('og:')) {
				this._meta.updateTag({ property: key, content: value });
			} else if (key.startsWith('twitter:')) {
				this._meta.updateTag({ name: key, content: value });
			} else {
				this._meta.updateTag({ [key]: value });
			}
		}
	}
}
