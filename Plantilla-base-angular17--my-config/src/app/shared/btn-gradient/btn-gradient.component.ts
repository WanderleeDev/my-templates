import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
	selector: 'app-btn-gradient',
	standalone: true,
	imports: [CommonModule],
	template: `
		<button
			class="text-[#303030] py-2 px-4 my-4 rounded-lg font-bold cursor-pointer bg-gradient-to-r from-[#F51DC1] to-[#2DFAFA] hover:scale-105 active:scale-95 transition-transform"
			type="button"
			title="to home"
			aria-label="to home"
		>
			Back to Home
		</button>
	`,
	styles: ':host { display: contents; }',
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class BtnGradientComponent {}
