# Template Angular 18

Last update 26-09-25

## Enable server-side rendering (optional)

The template is by default ready to work in Client Side Rendering (CSR) if you want the new features that Angular offers for Server Side Rendering (SSR) you just have to run the following schematic, it will update and configure your project for SSR.


```sh
ng add @angular/ssr
```

## Technologies included

- TailwindCss
- Eslint
- Prettier
- Error tailor

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.


## Estructure Folder

```
📁 angular-18
    📁 .vscode
    📁 public
        📁 assets
    📁 src
        📁 app
            📁 config
                📁 interfaces
            📁 core
                📁 models
                📁 services
                    📁 http
                    📁 seo
                📁 utils
                ─ info.txt
            📁 layout
                ─ info.txt
            📁 pages
                📁 home
                📁 notFound
                ─ info.txt
            📁 shared
                📁 components
                    📁 btn-base
                    📁 control-error
                📁 interfaces
                📁 ui
                    📁 btn-gradient
                ─ info.txt
            ─ app.component.ts
            ─ app.config.ts
            ─ app.routes.ts
        📁 environments
        ─ index.html
        ─ main.ts
        ─ styles.css
```
