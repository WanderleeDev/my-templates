import { CommonModule } from '@angular/common';
import {
	ChangeDetectionStrategy,
	Component,
	OnInit,
	inject,
} from '@angular/core';
import { SeoService } from '../../core/services/seo/Seo.service';
import { IMetadata, IOpenGraph } from '../../core/models/IMetadata.interface';

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
	private readonly _metaTags: Partial<IMetadata> = {
		author: 'Wanderlee Max Gutierrez Gamboa',
		description: 'Página de inicio',
		keywords: 'Angular, TypeScript, SEO',
	};
	private readonly _ogTags: Partial<IOpenGraph> = {
		'og:title': 'Titulo de la página',
		'og:description': 'Descripción de la página',
		'og:type': 'website', // El tipo de contenido.
		'og:site_name': 'Url de la página',
		'og:image':
			'https://www.dropbox.com/scl/fi/8afgokhtr6a97yg9jhyyy/mc-pixel-screen.webp?rlkey=gevljhx3imdt7zem5i05djkow&raw=1', // La URL de la imagen que quieres que se muestre en la vista previa
	};

	ngOnInit(): void {
		this._seoSvc.setTitle('Página de inicio');
		this._seoSvc.setCanonicalURL(window.location.href);
		this._seoSvc.applyIndexFollow();
		this._seoSvc.updateMetaTags({
			metaTags: this._metaTags,
			ogTags: this._ogTags,
		});
	}
}
