import { Routes } from '@angular/router';

export const routes: Routes = [
	{
		path: '',
		loadComponent: async () => import('./Pages/home/home.component'),
		title: 'Home',
	},
	{
		path: '**',
		loadComponent: async () => import('./Pages/notFound/notFound.component'),
		title: 'Not Found',
	},
];
