import { Routes } from '@angular/router';

export const routes: Routes = [
	{
		path: '',
		redirectTo: 'home',
		pathMatch: 'full',
	},
	{
		path: 'home',
		loadComponent: async () => import('./Pages/home/home.component'),
	},
	{
		path: '**',
		loadComponent: async () => import('./Pages/notFound/notFound.component'),
	},
];
