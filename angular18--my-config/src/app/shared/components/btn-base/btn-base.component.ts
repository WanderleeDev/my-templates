import { ChangeDetectionStrategy, Component, input } from '@angular/core';
import { ButtonProps } from '../../interfaces/ButtonProps.interface';

@Component({
	selector: 'app-btn-base',
	standalone: true,
	imports: [],
	templateUrl: './btn-base.component.html',
	styles: `
		:host {
			display: contents;
		}
	`,
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class BtnBaseComponent implements ButtonProps {
	props = input.required<Partial<HTMLButtonElement>>();
	label = input.required<string>();
}
