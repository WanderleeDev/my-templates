import { CommonModule, NgOptimizedImage } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BtnGradientComponent } from '../../shared/btn-gradient/btn-gradient.component';

@Component({
  selector: 'app-not-found',
  standalone: true,
  imports: [CommonModule, NgOptimizedImage, RouterLink, BtnGradientComponent],
  templateUrl: './notFound.component.html',
  styles: ':host { display: contents; }',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export default class NotFoundComponent {
  readonly url = window.location.href;
}
