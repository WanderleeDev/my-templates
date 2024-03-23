import { Injectable } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';
import { IMetaTagConfig } from '../../models/IMetadata.interface';

@Injectable({
	providedIn: 'root',
})
export class SeoService {
	constructor(
		private readonly _title: Title,
		private readonly _meta: Meta
	) {}

	public setCanonicalURL(url: string): void {
		if (URL.canParse(url)) {
			this._meta.updateTag({ name: 'canonical', content: url });
		}
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

	public updateMetaTags({ metaTags, ogTags }: IMetaTagConfig): void {
		console.log(metaTags, ogTags);
	}
}
