# Template Angular 17

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 17.0.0.

## Technologies included
- TailwindCss
- Eslint
- Prettier

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Enable server-side rendering (optional)

To add SSR to an existing project, use the Angular CLI ng add command.

```sh
ng add @angular/ssr
```

These commands create and update application code to enable SSR and adds extra files to the project structure.

## Estructure Folder

```
📁 src
  📁 app
    📁 Layout
    📁 Pages
      📁 home
        ─ home.component.html
        ─ home.component.ts
        ─ home.routes.ts
      📁 notFound
        ─ notFound.component.html
        ─ notFound.component.ts
      ─ app.component.ts
      ─ app.config.ts
      ─ app.routes.ts
    📁 core
      📁 guards
      📁 interceptors
      📁 models
        ─ IMetadata.interface.ts
      📁 services
        📁 http
          ─ http.service.ts
        📁 seo
          ─ Seo.service.ts
      📁 utils
        ─ validateUrl.ts
    📁 shared
      📁 UI
        📁 btn-gradient
          ─ btn-gradient.component.ts
      📁 directives
      ─ pipes
  📁 assets
      ─ .gitkeep
  📁 environments
    ─ environment.development.ts
    ─ environment.ts
  ─ favicon.ico
  ─ index.html
  ─ main.ts
  ─ styles.css
```
