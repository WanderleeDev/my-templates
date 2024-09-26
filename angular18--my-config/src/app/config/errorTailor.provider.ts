import { provideErrorTailorConfig } from '@ngneat/error-tailor';
import { MinlengthError } from './interfaces/MinlengthError.interface';
import { ControlErrorComponent } from '../shared/components/control-error/control-error.component';

const minlengthHandler = ({
	actualLength,
	requiredLength,
}: MinlengthError): string => {
	return `Expect ${requiredLength} but got ${actualLength}`;
};

const emailHandler = (error: string): string => `Email isn't valid - ${error}`;

export const errorTaylorProvider = provideErrorTailorConfig({
	errors: {
		useValue: {
			required: 'This field is required',
			minlength: minlengthHandler,
			invalidAddress: emailHandler,
		},
	},
	controlErrorComponent: ControlErrorComponent,
});
