import { ChangeDetectionStrategy, Component, input } from '@angular/core';
import { DefaultControlErrorComponent } from '@ngneat/error-tailor';

@Component({
	selector: 'app-control-error',
	standalone: true,
	imports: [],
	template: `
		<small [title]="message()" class="{{ errorMessageStyles }}">
			{{ message() }}
		</small>
	`,
	styles: `
		:host {
			display: block;
		}
	`,
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ControlErrorComponent extends DefaultControlErrorComponent {
	message = input.required<string>();
	errorMessageStyles =
		'text-xs border border-red-600 p-1 tracking-wider text-red-600 bg-red-100 block';
}
