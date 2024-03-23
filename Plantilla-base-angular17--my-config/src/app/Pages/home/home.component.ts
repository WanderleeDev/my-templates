import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
	selector: 'app-home',
	standalone: true,
	imports: [CommonModule],
	templateUrl: './home.component.html',
	styles: ':host { display: contents; }',
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export default class HomeComponent {}
