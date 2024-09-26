import { Routes } from '@angular/router';

export const routes: Routes = [
	{
		path: '',
		loadComponent: async () => import('./pages/home/home.component'),
		title: 'Home',
	},
	{
		path: '**',
		loadComponent: async () => import('./pages/notFound/notFound.component'),
		title: 'Not Found',
	},
];
