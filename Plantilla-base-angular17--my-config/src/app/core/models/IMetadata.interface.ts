export interface IMetadata {
	[key: string]: string;
	title: string;
	description: string;
	keywords: string;
	author: string;
}

export interface IOpenGraGraph {
	[key: string]: string;
}

export interface IMetaTagConfig {
	metaTags: Partial<IMetadata>;
	ogTags: Partial<IOpenGraGraph>;
}
