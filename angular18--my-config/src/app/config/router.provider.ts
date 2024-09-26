import {
	provideRouter,
	withViewTransitions,
	withComponentInputBinding,
} from '@angular/router';
import { routes } from '../app.routes';

export const routerProvider = provideRouter(
	routes,
	withViewTransitions({
		skipInitialTransition: true,
	}),
	withComponentInputBinding()
);
