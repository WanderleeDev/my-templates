import { ChangeDetectionStrategy, Component } from '@angular/core';
import { BtnBaseComponent } from '../../components/btn-base/btn-base.component';

@Component({
	selector: 'app-btn-gradient',
	standalone: true,
	imports: [BtnBaseComponent],
	template: `
		<app-btn-base
			label="Back to Home"
			[props]="{
				className: btnGradientStyles,
				ariaLabel: 'to home',
			}"
		/>
	`,
	styles: ':host { display: contents; }',
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class BtnGradientComponent {
	readonly btnGradientStyles =
		'text-[#303030] py-2 px-4 my-4 rounded-lg font-bold cursor-pointer bg-gradient-to-r from-[#F51DC1] to-[#2DFAFA] hover:scale-105 active:scale-95 transition-transform';
}
