export interface IMetaIndex {
	[key: string]: string;
}

export interface IMetadata extends IMetaIndex {
	description: string;
	keywords: string;
	author: string;
}

export interface IOpenGraph extends IMetaIndex {
	'og:title': string;
	'og:description': string;
	'og:url': string;
	'og:image': string;
	'og:video': string;
	'og:type': string;
	'og:site_name': string;
	'og:audio': string;
	'twitter:card': string;
	'twitter:site': string;
	'twitter:title': string;
	'twitter:description': string;
	'twitter:image': string;
}

export interface IMetaTagConfig {
	metaTags: Partial<IMetadata>;
	ogTags: Partial<IOpenGraph>;
}
