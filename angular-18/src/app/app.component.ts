import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgxSonnerToaster } from 'ngx-sonner';

@Component({
	selector: 'app-root',
	standalone: true,
	imports: [RouterOutlet, NgxSonnerToaster],
	template: `
		<ng-container>
			<router-outlet />
			<ngx-sonner-toaster richColors="true" />
		</ng-container>
	`,
})
export class AppComponent {}
