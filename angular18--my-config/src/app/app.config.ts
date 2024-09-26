import { ApplicationConfig } from '@angular/core';
import {
	errorTaylorProvider,
	httpClientProvider,
	routerProvider,
} from './config';

export const appConfig: ApplicationConfig = {
	providers: [errorTaylorProvider, httpClientProvider, routerProvider],
};
