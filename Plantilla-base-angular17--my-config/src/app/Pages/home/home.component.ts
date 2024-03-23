import { CommonModule } from '@angular/common';
import {
	ChangeDetectionStrategy,
	Component,
	OnInit,
	inject,
} from '@angular/core';
import { SeoService } from '../../core/services/seo/Seo.service';

@Component({
	selector: 'app-home',
	standalone: true,
	imports: [CommonModule],
	templateUrl: './home.component.html',
	styles: ':host { display: contents; }',
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export default class HomeComponent implements OnInit {
	private readonly _seoSvc = inject(SeoService);

	ngOnInit(): void {
		this._seoSvc.setTitle('Página de inicio');
		this._seoSvc.setCanonicalURL(window.location.href);
		this._seoSvc.applyIndexFollow();
	}
}
