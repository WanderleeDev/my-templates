import { ChangeDetectionStrategy, Component, inject } from '@angular/core';
import { SeoService } from '../../core/services/seo/Seo.service';
import { IMetadata, IOpenGraph } from '../../core/models/IMetadata.interface';
import { toast } from 'ngx-sonner';
import { BtnBaseComponent } from '../../shared/components/btn-base/btn-base.component';
import { ControlErrorComponent } from '../../shared/components/control-error/control-error.component';

@Component({
	selector: 'app-home',
	standalone: true,
	imports: [BtnBaseComponent, ControlErrorComponent],
	templateUrl: './home.component.html',
	styles: ':host { display: contents; }',
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export default class HomeComponent {
	#seoSvc = inject(SeoService);
	#metaTags: Partial<IMetadata> = {
		author: 'Wanderlee Max Gutierrez Gamboa',
		description: 'Página de inicio',
		keywords: 'Angular, TypeScript, SEO',
	};
	#ogTags: Partial<IOpenGraph> = {
		'og:title': 'Titulo de la página',
		'og:description': 'Descripción de la página',
		'og:type': 'El tipo de contenido ejemplo: website',
		'og:site_name': 'Url de la página',
		'og:image': 'URL de la imagen que se mostrara en la vista previa',
		// more options
	};

	constructor() {
		this.#seoSvc.setTitle('Página de inicio');
		this.#seoSvc.setCanonicalURL(window.location.href);
		this.#seoSvc.applyIndexFollow();
		this.#seoSvc.updateMetaTags({
			metaTags: this.#metaTags,
			ogTags: this.#ogTags,
		});
	}

	//  method test
	public onClick(): void {
		toast.success('Hola mundo', {
			description: 'Este es un toast de prueba',
		});
	}
}
