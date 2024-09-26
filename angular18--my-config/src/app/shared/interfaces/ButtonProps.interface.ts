import { InputSignal } from '@angular/core';

export interface ButtonProps {
	props: InputSignal<Partial<HTMLButtonElement>>;
	label: InputSignal<string>;
}
