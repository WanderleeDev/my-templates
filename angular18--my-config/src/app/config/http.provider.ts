import { provideHttpClient, withFetch } from '@angular/common/http';

export const httpClientProvider = provideHttpClient(withFetch());
