import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root',
})
export class HttpService {
	private readonly _http = inject(HttpClient);

	public getDAta<T>(url: string): Observable<T> {
		return this._http.get<T>(url);
	}
}
