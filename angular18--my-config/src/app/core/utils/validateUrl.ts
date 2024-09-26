export default function validateURL(url: string): boolean | never {
	if (!URL.canParse(url)) throw new Error(`Invalid URL: ${url}`);

	return true;
}
