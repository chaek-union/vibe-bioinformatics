# 7장. 생명정보 웹 툴 제작 기초

## 7.1 웹 도구, 아직 만들어야 하는가?

생명정보학에서 웹 도구는 오랫동안 **접근성의 관문** 역할을 해왔다. NCBI BLAST, Ensembl Genome Browser, Galaxy, UCSC Genome Browser 같은 도구들은 명령줄에 익숙하지 않은 실험 생물학자도 시퀀스 검색, 게놈 탐색, 분석 파이프라인 실행을 할 수 있게 만들었다. 웹 도구가 없었다면, 생명정보학은 소수의 전문 프로그래머만 접근할 수 있는 분야로 남았을 것이다.

그러나 이 장에서 웹 도구를 만들기 전에, 한 가지 질문을 던져야 한다. **AI 시대에도 웹 도구를 만드는 것이 여전히 의미가 있는가?**

웹(World Wide Web)은 30년 넘게 정보 공유의 기본 플랫폼이었다. 그러나 **Web 4.0**(AI가 주도하는 지능형 웹)에 대한 논의가 이어지면서, 전통적인 웹 인터페이스의 미래에 의문이 제기되고 있다. 사람이 아니라 봇과 AI 에이전트가 웹에 접근하는 경우도 점점 늘고 있다. MCP와 같은 프로토콜이 보편화되면, AI 에이전트가 웹 브라우저를 거치지 않고 데이터와 서비스에 직접 접근하는 시대가 올 것이다. 그때 화려한 UI와 반응형 디자인은 더 이상 중요하지 않을 수 있다.

그럼에도 불구하고, 웹 도구를 배우는 것에는 몇 가지 현실적인 이유가 있다:

- **시각화와 인터랙션**: BLAST 검색 결과를 표로 보여주고, 시퀀스 정렬을 시각화하고, 파라미터를 조정하며 분석을 반복하는 작업은 여전히 GUI가 효과적이다. 터미널에서 텍스트로만 작업하는 것보다 직관적이다.
- **공유와 접근성**: 웹 도구가 생명정보학의 접근성을 높여온 것처럼, 직접 만든 분석 도구도 "이 URL을 열어보세요" 한마디로 동료와 공유할 수 있다.
- **풀스택 이해**: 프론트엔드, 백엔드, 데이터베이스, API를 아우르는 웹 개발 경험은 MCP 서버를 만들거나 AI 에이전트의 도구를 설계할 때도 직접적으로 활용된다.
- **바이브 코딩 실습**: 웹 개발은 AI 에이전트와 협업하는 훈련장으로 적합하다. 결과물이 눈에 보이므로 AI가 생성한 코드의 품질을 즉시 판단할 수 있다.

결론적으로, 웹 인터페이스 자체의 중요성은 점차 줄어들겠지만, **웹 도구를 만드는 과정에서 익히는 기술과 사고방식**은 AI 시대에도 유효하다. 이 장에서는 생명정보학 웹 도구의 기반이 되는 프로젝트를 구성한다.

## 7.2 이 책에서 사용하는 기술 스택

이 책에서는 다음과 같은 기술 스택을 사용하여 생명정보학 웹 도구를 개발한다.

| 기술 | 역할 | 설명 |
|------|------|------|
| **SvelteKit** | 프론트엔드 프레임워크 | 빠르고 가벼운 웹 앱 개발 프레임워크 |
| **Tailwind CSS** | CSS 프레임워크 | 유틸리티 클래스 기반의 스타일링 도구 |
| **PostgreSQL** | 데이터베이스 | 오픈소스 관계형 데이터베이스 |
| **Docker** | 컨테이너 | 개발 환경 통합 관리 |

이 조합을 선택한 이유는 바이브 코딩에 적합하기 때문이다. SvelteKit은 코드량이 적어 AI가 생성하고 수정하기 쉽고, Tailwind CSS는 스타일 정보가 HTML과 같은 파일에 있어 AI가 맥락을 파악하기 용이하다. PostgreSQL은 안정적이고 널리 사용되는 데이터베이스이므로 AI가 정확한 SQL을 생성할 확률이 높다.

> **버전 안내**: 이 책은 SvelteKit 3, Svelte 5(runes), Tailwind CSS 4, Node 24 LTS 기준으로 작성되었다. 웹 프레임워크는 빠르게 바뀌므로, 책의 명령이나 코드가 그대로 동작하지 않으면 공식 문서(https://svelte.dev/docs, https://tailwindcss.com/docs, https://nodejs.org)를 먼저 확인한다.

### SvelteKit

SvelteKit은 Svelte를 기반으로 한 풀스택 웹 프레임워크이다. "풀스택"이란 프론트엔드(사용자가 보는 화면)와 백엔드(서버 로직, 데이터베이스 연동)를 하나의 프레임워크에서 모두 처리할 수 있다는 뜻이다.

React, Vue 등 다른 프레임워크와 비교했을 때 다음과 같은 장점이 있다:

- **컴파일 타임 최적화**: React는 브라우저에서 가상 DOM을 비교하며 화면을 갱신하지만, Svelte는 빌드 시점에 컴포넌트를 최적화된 JavaScript로 변환한다. 가상 DOM 비교 과정이 없으므로 브라우저가 해야 할 일이 적다.
- **적은 코드량**: 같은 기능을 비교적 짧은 코드로 구현할 수 있다. 이는 AI가 생성하는 코드량이 줄어든다는 뜻이기도 하다. 코드가 짧으면 검토하기 쉽고 에러가 날 가능성도 줄어든다.
- **서버 사이드 렌더링(SSR)** 기본 지원: 페이지를 서버에서 미리 렌더링하여 브라우저에 전달하므로, 첫 화면 로딩이 빠르다.
- **파일 기반 라우팅**: 파일 구조가 곧 URL 구조이다. `src/routes/tools/blast/+page.svelte` 파일을 만들면 자동으로 `/tools/blast` URL이 생긴다. URL 설정을 위한 별도 파일이 필요 없다.

![SvelteKit 공식 웹사이트](../assets/ch7-01-sveltekit-website.png)

SvelteKit에서 페이지는 크게 세 가지 파일로 구성된다:

| 파일 | 역할 | 실행 위치 |
|------|------|-----------|
| `+page.svelte` | 사용자에게 보이는 화면 (HTML + CSS + JS) | 브라우저 |
| `+page.server.ts` | 데이터 로딩, 폼 처리 등 서버 로직 | 서버 |
| `+server.ts` | REST API 엔드포인트 | 서버 |

예를 들어 BLAST 검색 도구를 만든다면, `+page.svelte`에는 시퀀스 입력 폼과 결과 테이블을, `+page.server.ts`에는 BLAST+ 명령 실행과 결과 파싱 로직을 작성한다. 이 구분을 이해하고 있으면, AI에게 "서버 로직에 BLAST 검색 기능 추가해줘"라고 구체적으로 요청할 수 있다.

Svelte 5에서는 **룬(rune)**이라고 부르는 `$`로 시작하는 특수 문법으로 컴포넌트의 상태를 다룬다:

| 룬 | 역할 | 예시 |
|----|------|------|
| `$state` | 값이 바뀌면 화면이 자동으로 갱신되는 상태 | `let count = $state(0);` |
| `$derived` | 다른 상태에서 자동으로 계산되는 값 | `let double = $derived(count * 2);` |
| `$props` | 부모 컴포넌트가 넘겨준 값 | `let { title } = $props();` |

`npx sv create`로 만든 새 프로젝트는 모든 컴포넌트를 runes 모드로 컴파일한다. 인터넷 자료나 AI가 제시하는 Svelte 4 문법(`export let`, `on:click`, `<slot />`, `$:`)은 runes 모드에서 경고나 에러를 낸다. AI가 이런 문법을 쓰면 "Svelte 5 runes 문법으로 바꿔줘"라고 요청한다.

### Tailwind CSS

Tailwind CSS는 유틸리티 클래스 기반의 CSS 프레임워크이다. 전통적인 CSS에서는 별도의 스타일시트 파일을 만들고 클래스 이름을 정의한 후 스타일을 작성한다. Tailwind는 이 과정을 생략하고, 미리 정의된 유틸리티 클래스를 HTML 요소에 직접 적용한다.

```html
<!-- 전통적인 CSS 방식 -->
<div class="card">제목</div>

<!-- Tailwind CSS 방식 -->
<div class="bg-white rounded-lg shadow-md p-6">제목</div>
```

Tailwind 방식에서 `bg-white`는 흰색 배경, `rounded-lg`는 둥근 모서리, `shadow-md`는 중간 크기 그림자, `p-6`은 패딩 1.5rem을 의미한다. 클래스 이름만 보면 어떤 스타일이 적용되는지 알 수 있다.

AI 에이전트와 함께 사용하기에 특히 적합한데, 스타일이 HTML과 같은 파일에 있어 컨텍스트를 파악하기 쉽기 때문이다. 전통적인 CSS에서는 AI가 HTML 파일과 CSS 파일을 모두 읽어야 전체 디자인을 이해할 수 있지만, Tailwind에서는 HTML 파일 하나만 읽으면 된다.

![Tailwind CSS 공식 웹사이트](../assets/ch7-02-tailwindcss-website.png)

### PostgreSQL

PostgreSQL은 가장 널리 쓰이는 오픈소스 관계형 데이터베이스 중 하나이다. "관계형"이란 데이터를 표(테이블) 형태로 저장하고, 테이블 간의 관계를 정의할 수 있다는 뜻이다.

이 책에서 PostgreSQL은 다음과 같은 용도로 사용된다:
- **분석 결과 저장**: BLAST 검색 결과, 차등 발현 분석 결과 등
- **사용자 데이터 관리**: 사용자가 업로드한 시퀀스 정보
- **작업 이력 추적**: 누가 언제 어떤 분석을 실행했는지

SQLite 같은 가벼운 데이터베이스도 있지만, PostgreSQL을 선택한 이유는 실무 환경과 동일한 경험을 제공하기 위해서이다. Docker를 통해 실행하므로 설치가 번거롭지도 않다.

## 7.3 프로젝트 생성

### Node.js 설치

SvelteKit은 JavaScript/TypeScript 기반이므로 Node.js가 필요하다. Node.js는 브라우저 밖에서 JavaScript를 실행할 수 있게 해주는 런타임이다. 다음 웹사이트에서 설치한다:

https://nodejs.org/en/download

다운로드 페이지 상단에서 버전, 운영체제, 설치 방법, 패키지 매니저를 차례로 고른다. **Windows 사용자도 WSL 환경에서 개발하므로 운영체제는 Linux를 선택**해야 한다. 버전은 이 책의 기준인 **v24 LTS**를 고르고, 설치 방법은 **nvm**(Node Version Manager), 패키지 매니저는 **pnpm**을 선택한 후 터미널에 표시되는 명령을 입력한다. 페이지가 기본으로 보여주는 LTS 버전이 더 높아도 대부분 그대로 동작하지만, SvelteKit 3은 Node 22.17 이상을 요구하므로 그보다 낮은 버전은 피한다. nvm은 여러 버전의 Node.js를 설치하고 전환할 수 있게 해주는 도구이다. 프로젝트마다 다른 Node.js 버전이 필요할 수 있으므로, 직접 설치보다 nvm을 통한 설치가 권장된다.

pnpm은 npm의 대안으로, 디스크 공간을 절약하고 설치 속도가 빠르다. 여러 프로젝트에서 같은 패키지를 사용할 때, pnpm은 패키지를 한 번만 다운로드하고 심볼릭 링크로 연결한다.

Node 24에서는 다운로드 페이지가 안내하는 `corepack enable pnpm` 명령으로 pnpm을 켤 수 있다. corepack은 Node 24까지 Node.js에 함께 들어 있는 도구이다. Node 25부터는 corepack이 함께 배포되지 않으므로, 더 높은 버전을 설치했다면 `npm install -g pnpm`으로 pnpm을 설치한다.

![Node.js 다운로드 페이지](../assets/ch7-03-nodejs-nvm-pnpm.png)

설치 확인:

```bash
node --version
pnpm --version
```

### SvelteKit 프로젝트 초기화

터미널에서 다음 명령을 실행하여 SvelteKit 프로젝트를 생성한다:

```bash
npx sv create my-bioinfo-app
```

CLI가 대화형으로 옵션을 물어본다. 방향키와 스페이스바로 선택하고 엔터로 진행한다:

| 질문 | 선택 |
|------|------|
| Which template would you like? | **SvelteKit minimal** |
| Add type checking with TypeScript? | **Yes, using TypeScript syntax** |
| What would you like to add to your project? | **tailwindcss, sveltekit-adapter, paraglide** |
| tailwindcss: Which plugins would you like to add? | **typography, forms** |
| sveltekit-adapter: Which SvelteKit adapter would you like to use? | **node** |
| paraglide: Which languages would you like to support? | **en, ko** (기본값 en, es를 지우고 입력) |
| paraglide: Do you want to include a demo? | **No** (기본값은 Yes) |
| Which package manager do you want to install dependencies with? | **pnpm** |

질문에 하나씩 답하는 대신, 같은 선택을 옵션으로 지정하여 한 줄로 실행할 수도 있다:

```bash
npx sv create my-bioinfo-app --template minimal --types ts --add tailwindcss="plugins:typography,forms" sveltekit-adapter="adapter:node" paraglide="languageTags:en,ko+demo:no" --install pnpm
```

프로젝트 생성이 완료되면, VS Code에서 **파일 → 폴더 열기**로 `my-bioinfo-app` 디렉토리를 연다.

각 옵션의 역할을 간단히 정리하면:

- **TypeScript**: JavaScript에 타입 시스템을 추가한 언어. AI가 생성하는 코드에서도 타입이 있으면 잘못된 데이터 사용을 컴파일 시점에 잡아낼 수 있다.
- **Tailwind CSS**: 유틸리티 클래스 기반 CSS 프레임워크. Typography 플러그인은 마크다운 렌더링 시 보기 좋은 기본 스타일을, Forms 플러그인은 폼 요소에 기본 스타일을 적용한다.
- **sveltekit-adapter (node)**: SvelteKit 앱을 Node.js 서버로 배포할 수 있게 해주는 어댑터.
- **Paraglide**: 다국어(i18n) 지원 라이브러리. 영어(en)와 한국어(ko)를 지원하도록 설정한다.

> **참고**: 프로젝트 초기 생성은 AI 에이전트에 맡기기보다 직접 수행하는 것이 좋다. AI는 초기화 명령을 사용하기보다 기존 코드를 직접 작성하려는 경향이 있어, 최신 버전이 아닌 코드를 생성할 수 있다. 프로젝트 뼈대를 공식 CLI로 먼저 만들고, 그 위에서 AI에게 기능 추가를 요청하는 것이 안전하다.

### Tailwind CSS

Tailwind CSS는 SvelteKit 프로젝트 생성 시 옵션으로 함께 설치할 수 있다. 별도로 수동 설치할 필요 없이, 프로젝트 초기화 과정에서 Tailwind CSS를 선택하면 자동으로 설정된다. Typography 플러그인은 마크다운 렌더링 시 보기 좋은 기본 스타일을 제공하고, Forms 플러그인은 폼 요소(입력 필드, 버튼 등)에 기본 스타일을 적용해 준다.

Tailwind CSS 4는 `tailwind.config.js` 같은 별도 설정 파일을 만들지 않고, CSS 파일 안에서 설정한다(CSS-first 방식). 프로젝트를 생성하면 `src/routes/layout.css`가 만들어지고, 공통 레이아웃(`src/routes/+layout.svelte`)이 이 파일을 불러온다:

```css
/* src/routes/layout.css */
@import 'tailwindcss';
@plugin '@tailwindcss/forms';
@plugin '@tailwindcss/typography';
```

`@import`는 Tailwind를 불러오고, `@plugin`은 플러그인을 추가한다. 프로젝트의 기본 색상이나 폰트를 정하고 싶다면 같은 파일에 `@theme` 블록을 추가한다:

```css
@theme {
  --color-primary: #2563eb;
}
```

이렇게 정의하면 `bg-primary`, `text-primary` 같은 클래스를 바로 쓸 수 있다. AI가 `tailwind.config.js`를 새로 만들거나 `@tailwind base;` 같은 Tailwind 3 문법을 쓰면, "Tailwind CSS 4 방식으로 layout.css에서 설정해줘"라고 요청한다.

## 7.4 Docker 환경 구성

### compose.yml과 Dockerfile 생성

3장에서 배운 Docker Compose를 실전에 적용한다. Claude Code에게 다음과 같이 요청한다:

> "SvelteKit 앱과 PostgreSQL 데이터베이스를 Docker Compose로 구성해줘. compose.yml(배포용)과 compose.dev.yml(개발용)을 만들어줘. 앱 이미지는 node:24-alpine를 기반으로 하고, 개발용은 소스 코드를 볼륨으로 마운트해서 `pnpm dev --host`로 5173 포트에서 핫 리로드되게 해줘. 배포용은 adapter-node로 빌드한 결과를 `node build`로 3000 포트에서 실행해줘. 데이터베이스는 postgres:18 이미지를 사용해줘. Dockerfile도 함께 만들어줘."

이때 **compose.yml**(배포용)과 **compose.dev.yml**(개발용)을 분리하는 것이 좋다. 개발 환경에서는 코드 변경이 즉시 반영되어야 하지만, 배포 환경에서는 최적화된 빌드 결과만 실행하면 된다. 두 파일을 분리해 두면, 개발할 때는 `docker compose -f compose.dev.yml up`(http://localhost:5173)으로, 배포할 때는 `docker compose up`(http://localhost:3000)으로 실행할 수 있다. 5173은 Vite 개발 서버의 기본 포트이고, 3000은 adapter-node로 빌드한 서버의 기본 포트이다.

Claude Code가 생성하는 파일의 주요 설정을 이해해 두면, 결과를 검토하고 수정 요청을 내리기 쉽다:

| 설정 | 의미 |
|------|------|
| `ports: - "5173:5173"` | 개발 서버 포트를 호스트에 연결(compose.dev.yml). 배포용 compose.yml은 `"3000:3000"` |
| `volumes: - .:/app` | 로컬 코드를 컨테이너에 연결. 코드 수정 시 즉시 반영 |
| `/app/node_modules` | 컨테이너 자체의 node_modules 사용. 호스트와 충돌 방지 |
| `depends_on: - db` | db를 먼저 시작한 후 app 시작 |
| `pgdata:/var/lib/postgresql` | 컨테이너를 삭제해도 데이터베이스 보존. postgres 18 이미지부터는 예전처럼 `/var/lib/postgresql/data`에 마운트하면 컨테이너가 시작되지 않으므로 이 경로를 사용한다 |
| `DATABASE_URL` | 컨테이너 간 네트워크 주소. `db`는 서비스 이름 |

Dockerfile에서는 3장에서 배운 레이어 캐싱 원리가 적용된다. `package.json`을 먼저 복사하고 의존성을 설치한 뒤 소스 코드를 복사하면, 소스 코드만 변경되었을 때 의존성 설치 단계를 건너뛸 수 있다. `--host` 플래그는 Docker 컨테이너 내부 서버에 호스트에서 접속하기 위해 필요하다.

> **참고**: SvelteKit 3은 `src/env.ts`에 선언한 환경 변수(7.5절)의 값이 없으면 빌드와 실행을 멈춘다. Docker 이미지를 빌드하는 단계에는 보통 `.env`가 없으므로, 배포용 이미지 빌드가 `Invalid environment variables` 에러로 실패할 수 있다. 이때는 에러 메시지를 Claude Code에게 보여주고 수정을 요청한다. 빌드할 때만 값을 생략하는 방법은 공식 문서(https://svelte.dev/docs/kit/environment-variables)에 나와 있다.

## 7.5 환경 변수 (.env)

프로젝트에서 데이터베이스 접속 정보, API 키 등 민감한 설정값은 **환경 변수**로 관리한다. 코드에 비밀번호를 직접 쓰면 Git에 커밋될 위험이 있다. 환경 변수를 사용하면 코드와 설정을 분리할 수 있다.

> **중요**: `.env` 파일은 **반드시 사용자가 직접 작성해야 한다**. `.env`에는 데이터베이스 비밀번호, API 키 등 민감한 정보가 포함되므로, **Claude Code가 이 파일을 읽거나 생성하게 해서는 안 된다**.

가장 확실한 방법은 Claude Code 설정 파일에 **읽기 금지 규칙**(`permissions.deny`)을 넣는 것이다. 모든 프로젝트에 적용되도록 사용자 설정 파일 `~/.claude/settings.json`에 다음 내용을 추가한다(파일이 없으면 새로 만든다):

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)"
    ]
  }
}
```

이 규칙은 Claude Code 프로그램이 직접 강제하므로, AI가 판단을 잘못하더라도 `.env`를 읽을 수 없다. `Read(./.env.*)`는 `.env.local`, `.env.production` 같은 파일도 막는데, 아래에서 만들 `.env.example`도 여기에 포함된다. Claude Code가 `.env.example`은 참고할 수 있게 하려면 `"Read(./.env.*)"` 대신 `"Read(./.env.local)"`처럼 막을 파일을 하나씩 적는다. 설정 파일의 형식은 공식 문서(https://code.claude.com/docs/en/settings)에서 확인할 수 있다.

보조 수단으로 글로벌 `CLAUDE.md`(`~/.claude/CLAUDE.md`)에도 규칙을 적어 두면, AI가 처음부터 `.env`에 접근하려는 시도 자체를 줄일 수 있다. 다만 CLAUDE.md는 AI가 참고하는 지침일 뿐 강제력이 없으므로, 위의 설정과 함께 사용한다:

```
# 보안 규칙
- .env 파일을 읽거나 수정하지 말 것
- .env.example만 참조할 것
```

프로젝트 루트에 `.env` 파일을 직접 생성한다:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/bioinfo
SITE_NAME=My Bioinfo App
```

SvelteKit 3에서는 앱에서 사용할 환경 변수를 `src/env.ts` 파일에 선언한다. 이 파일에는 비밀 값이 아니라 변수의 이름과 공개 여부만 들어가므로, Claude Code에게 작성을 맡겨도 된다:

```ts
// src/env.ts
import { defineEnvVars } from '@sveltejs/kit/env';

export const variables = defineEnvVars({
  DATABASE_URL: {},
  SITE_NAME: { public: true }
});
```

선언한 변수는 공개 여부에 따라 서로 다른 모듈에서 가져온다:

| 선언 | 가져오는 모듈 | 접근 범위 | 용도 |
|------|---------------|-----------|------|
| `{}` (기본값) | `$app/env/private` | 서버만 | 데이터베이스 비밀번호, API 키 등 민감 정보 |
| `{ public: true }` | `$app/env/public` | 서버 + 클라이언트 | 사이트 이름 등 공개 정보 |

```ts
import { DATABASE_URL } from '$app/env/private'; // 서버 코드에서만 사용 가능
import { SITE_NAME } from '$app/env/public';     // 어디서나 사용 가능
```

`$app/env/private`는 서버 코드(`+page.server.ts`, `+server.ts`, `src/lib/server/` 안의 파일 등)에서만 가져올 수 있다. 브라우저에서 실행되는 코드에서 가져오면 빌드 단계에서 에러가 나므로, 데이터베이스 비밀번호나 API 키가 실수로 사용자에게 노출되지 않는다. 이 구분은 보안상 중요하다. 또한 `src/env.ts`에 선언한 변수가 `.env`에 없으면 개발 서버가 `Invalid environment variables` 에러를 내며 시작되지 않으므로, 빠뜨린 설정을 바로 알아챌 수 있다.

> **참고**: 이전 버전의 SvelteKit에서는 `PUBLIC_` 접두사와 `$env/static/private` 같은 모듈로 공개/비공개를 구분했다. 이 방식은 SvelteKit 3에서 deprecated되었으므로, AI가 이 문법을 쓰면 `src/env.ts` 방식으로 바꿔 달라고 요청한다.

`.env` 파일은 Git에 커밋되지 않도록 반드시 `.gitignore`에 포함되어 있어야 한다. `npx sv create`가 만든 `.gitignore`에는 이미 `.env`가 들어 있으므로, 이 줄이 지워지지 않았는지 확인한다. 대신 `.env.example` 파일을 만들어 어떤 환경 변수가 필요한지 안내한다. `.env.example`에는 실제 값 대신 템플릿을 넣는다. 이 파일은 Claude Code에게 생성을 요청해도 된다.

> "`.env.example` 파일을 만들어줘. DATABASE_URL과 SITE_NAME이 필요해."

## 7.6 프로젝트 디렉토리 구조

최종적으로 프로젝트 디렉토리는 다음과 같은 구조를 가진다:

```
my-bioinfo-app/
├── compose.yml             # Docker 서비스 정의 (배포용)
├── compose.dev.yml         # Docker 서비스 정의 (개발용)
├── Dockerfile              # Docker 이미지 정의
├── .env                    # 환경 변수 값 (Git에 포함하지 않음)
├── .env.example            # 환경 변수 템플릿
├── .gitignore
├── package.json            # 의존성, 스크립트, #lib 별칭(imports)
├── pnpm-lock.yaml
├── vite.config.ts          # Vite + SvelteKit 설정 (어댑터, runes 등)
├── tsconfig.json           # TypeScript 설정
├── CLAUDE.md               # AI 에이전트 참조용 프로젝트 명세
├── README.md
├── messages/               # Paraglide 번역 파일 (en.json, ko.json)
├── project.inlang/         # Paraglide 설정
├── src/
│   ├── app.html            # HTML 템플릿
│   ├── env.ts              # 환경 변수 선언
│   ├── hooks.server.ts     # 서버 훅 (Paraglide 언어 처리)
│   ├── hooks.ts            # 공통 훅 (Paraglide URL 처리)
│   ├── lib/                # 공유 라이브러리 (#lib)
│   │   ├── components/     # 재사용 가능한 컴포넌트
│   │   └── server/         # 서버 전용 코드 (DB 연결 등)
│   └── routes/             # 페이지 라우트
│       ├── layout.css      # 글로벌 스타일 (Tailwind 설정)
│       ├── +layout.svelte  # 공통 레이아웃
│       ├── +page.svelte    # 랜딩 페이지
│       └── tools/
│           └── +page.svelte  # 도구 페이지
└── static/                 # 정적 파일 (이미지, 폰트 등)
```

이 구조에서 가장 중요한 폴더는 `src/routes/`이다. SvelteKit의 파일 기반 라우팅에 의해, 이 폴더의 구조가 곧 웹사이트의 URL 구조가 된다. `src/routes/tools/blast/+page.svelte`를 만들면 `/tools/blast`라는 URL이 자동으로 생긴다. AI에게 새 페이지를 추가해 달라고 할 때, 이 규칙을 알면 "tools 폴더 아래에 blast 페이지를 만들어줘"라고 구체적으로 지시할 수 있다.

`src/lib/` 폴더는 여러 페이지에서 공유하는 코드를 넣는 곳이다. 예를 들어 네비게이션 바 컴포넌트는 모든 페이지에서 사용하므로 `src/lib/components/NavBar.svelte`에 둔다. 다른 파일에서는 `#lib` 별칭으로 가져온다. `import NavBar from '#lib/components/NavBar.svelte'`처럼 쓰면 파일이 어느 폴더에 있든 같은 경로로 가져올 수 있다. 이 별칭은 `package.json`의 `imports` 항목에 정의되어 있으며, 이전 버전의 SvelteKit에서 쓰던 `$lib`를 대신한다. `src/lib/server/`처럼 `server`라는 이름의 폴더에 둔 코드는 서버 전용으로 취급되어, 브라우저에서 실행되는 코드에서는 가져올 수 없다. 데이터베이스 연결 코드처럼 서버에서만 사용하는 코드는 이곳에 둔다.

목록에 `svelte.config.js`와 `tailwind.config.ts`가 없다는 점에도 주목하자. SvelteKit 3부터 프로젝트 설정(어댑터, 컴파일 옵션 등)은 `vite.config.ts`의 `sveltekit({ ... })` 안에 들어가고, Tailwind CSS 4는 `src/routes/layout.css`에서 설정한다. 인터넷 자료나 AI가 이 두 파일을 만들자고 하면 이전 버전을 기준으로 한 내용이라는 신호이다.

### CLAUDE.md 작성

`CLAUDE.md`는 AI 에이전트가 참조하는 프로젝트 명세 파일이다. Claude Code는 세션을 시작할 때마다 이 파일을 읽고, 프로젝트의 규칙을 파악한다.

**핵심 원칙: CLAUDE.md에는 AI가 코드만 읽어서는 알 수 없는 정보를 짧게 적는다.**

Claude Code는 프로젝트 파일을 직접 읽을 수 있다. 이 프로젝트가 SvelteKit을 쓰는지, Navbar 컴포넌트가 어디에 있는지, 스타일링에 Tailwind CSS를 쓰는지 같은 정보는 코드를 탐색하여 스스로 알아낸다. 반면 코드만 봐서는 알 수 없는 정보도 있다:

- 작업 결과를 확인하는 방법: 개발 서버 실행, 타입 검사, 테스트 명령
- 지켜야 할 규칙: Svelte 5 runes 문법만 사용, 환경 변수는 `src/env.ts`에 선언
- 사람이 내린 결정: primary 색상, 레이아웃 최대 너비 같은 디자인 가이드라인
- AI가 이미 두 번 이상 반복한 실수

CLAUDE.md는 모든 작업에 함께 읽히므로, 내용이 길어질수록 정작 중요한 규칙이 묻히기 쉽다. Claude Code 공식 문서도 CLAUDE.md를 짧게 유지하라고 권장한다(https://code.claude.com/docs/en/best-practices). 코드에서 알 수 있는 내용은 빼고, 위와 같은 정보만 간결하게 적는 것이 좋다.

#### 왜 배경지식이 필요한가?

바이브 코딩은 "AI가 다 해주니까 개발을 몰라도 된다"는 뜻이 **아니다**. 오히려 그 반대이다. CLAUDE.md를 잘 작성하려면 **사람이 먼저 프로젝트를 이해하고 있어야 한다**.

예를 들어 이런 CLAUDE.md를 작성한다고 하자:

```markdown
# 프로젝트 개요
생명정보학 웹 도구 모음 사이트 (SvelteKit 3, Svelte 5, Tailwind CSS 4, PostgreSQL)

# 명령
- 개발 서버: docker compose -f compose.dev.yml up (http://localhost:5173)
- 타입 검사: pnpm check

# 코딩 규칙
- Svelte 5 runes 문법만 사용 ($state, $derived, $props, onclick, {@render children()})
- Svelte 4 문법(export let, on:click, <slot />, $:) 사용 금지
- 공유 코드는 #lib 별칭으로 가져오기 ($lib 사용 금지)
- 환경 변수는 src/env.ts에 선언하고 $app/env/private, $app/env/public에서 가져오기
- Tailwind 설정은 src/routes/layout.css에서 (tailwind.config 파일 만들지 않기)

# 디자인 가이드라인
- 색상: blue-600을 primary color로 사용
- 레이아웃: 최대 너비 max-w-7xl, 중앙 정렬
- 반응형: mobile-first 접근
```

이 파일을 작성하려면 runes가 무엇인지, `#lib` 별칭과 환경 변수 선언이 어떻게 동작하는지, Tailwind의 유틸리티 클래스와 반응형 디자인이 무엇인지 알아야 한다. 특히 "코딩 규칙"의 각 줄은 AI가 이전 버전의 문법을 쓰는 실수를 막기 위한 것인데, 이전 버전과 현재 버전의 차이를 알아야 이런 규칙을 적을 수 있다. **이 책에서 배우는 웹 개발 배경지식이 바로 이를 위한 것이다.**

> **핵심**: 바이브 코딩에서 사람의 역할은 코드를 직접 작성하는 것이 아니라, **AI가 올바른 코드를 작성할 수 있도록 정확한 지시를 내리는 것**이다. 정확한 지시를 내리려면 기본적인 개발 개념을 이해하고 있어야 한다.

#### CLAUDE.md에 포함할 내용

| 항목 | 설명 | 예시 |
|------|------|------|
| **프로젝트 개요** | 목적과 사용 기술을 한두 줄로 | "생명정보학 연구자를 위한 웹 기반 시퀀스 분석 도구" |
| **명령** | 개발 서버 실행, 타입 검사, 테스트 방법 | "타입 검사: pnpm check" |
| **코딩 규칙** | 코드만 봐서는 알 수 없는 규칙, 쓰지 말아야 할 이전 문법 | "Svelte 5 runes 문법만 사용" |
| **디자인 가이드라인** | 색상, 폰트, 레이아웃 규칙 | "primary color는 blue-600, 최대 너비 max-w-7xl" |
| **도메인 규칙** | 생명정보학 관련 규칙 | "FASTA 형식은 >로 시작하는 헤더 + 시퀀스" |

CLAUDE.md는 한 번 작성하고 끝이 아니다. 프로젝트가 발전할수록 새로운 규칙이 생기고, 더 이상 필요 없는 규칙도 생긴다. AI가 같은 실수를 반복하면 그 내용을 한 줄로 추가하고, 의미가 없어진 줄은 지워서 파일을 짧게 유지한다. 이렇게 CLAUDE.md를 관리하는 것이 바이브 코딩에서 사람의 중요한 역할이다.

> **팁**: CLAUDE.md를 처음부터 직접 쓸 필요는 없다. Claude Code에서 `/init` 명령을 실행하면 현재 코드를 분석하여 CLAUDE.md 초안을 만들어 준다. 초안에서 코드만 봐도 알 수 있는 내용은 지우고, 위의 "코딩 규칙"처럼 AI가 알 수 없는 내용을 더하는 방식으로 다듬는다.

## 7.7 개발 서버 실행

### Docker를 사용하는 경우

```bash
docker compose -f compose.dev.yml up
```

브라우저에서 `http://localhost:5173`으로 접속하면 SvelteKit 앱을 확인할 수 있다. 최초 실행 시 Docker 이미지 빌드와 의존성 설치에 몇 분이 걸릴 수 있지만, 두 번째 실행부터는 캐시 덕분에 수 초 만에 시작된다.

배포용 설정으로 실행해 보려면 `docker compose up`을 사용한다. 이때는 빌드된 adapter-node 서버가 실행되므로 `http://localhost:3000`으로 접속한다. 코드를 수정해도 바로 반영되지 않으므로, 개발 중에는 compose.dev.yml을 사용한다.

### Docker 없이 로컬에서 실행하는 경우

```bash
pnpm dev
```

Docker 없이도 개발 서버를 실행할 수 있지만, 이 경우 PostgreSQL을 별도로 설치하고 실행해야 한다. 또한 `src/env.ts`에 선언한 변수가 `.env`에 모두 들어 있어야 개발 서버가 시작된다. Docker를 사용하면 `docker compose -f compose.dev.yml up` 한 줄로 웹 서버와 데이터베이스가 모두 시작되므로 더 편리하다.

![SvelteKit 개발 서버 실행 화면](../assets/ch7-04-sveltekit-dev-server.png)

## 7.8 보안 점검

웹 도구를 만들면 누구나 브라우저로 접속할 수 있게 된다. 문제는 모든 사용자가 선의로 사용하지는 않는다는 것이다. 웹 보안에서 자주 등장하는 공격 유형을 알아두면, AI에게 점검을 요청할 때도 맥락을 이해할 수 있다.

- **SQL 인젝션**: 검색창에 일반 검색어 대신 데이터베이스 명령어를 입력하는 공격이다. 예를 들어 로그인 폼에 `' OR 1=1 --`을 입력하면, 비밀번호 확인 없이 로그인이 될 수 있다. 사용자 입력을 그대로 데이터베이스 쿼리에 넣으면 이런 문제가 발생한다.
- **XSS(크로스 사이트 스크립팅)**: 게시판이나 댓글에 `<script>` 태그를 삽입하여, 다른 사용자의 브라우저에서 악성 코드가 실행되게 하는 공격이다. 사용자 입력을 검증 없이 화면에 출력하면 위험하다.
- **명령 주입**: 10장에서 만들 BLAST 도구처럼, 사용자 입력을 시스템 명령에 전달하는 경우가 있다. 이때 입력값에 `; rm -rf /` 같은 명령을 끼워 넣으면 서버에서 의도하지 않은 명령이 실행될 수 있다.
- **관리자 페이지 노출**: `/admin`, `/dashboard`, `/api/users` 같은 흔한 URL 패턴은 공격자가 가장 먼저 시도하는 경로다. 관리자 기능이 이런 예측 가능한 URL에 인증 없이 노출되어 있으면, 누구든 접근할 수 있게 된다.
- **CORS 설정 미비**: CORS(Cross-Origin Resource Sharing)는 다른 도메인에서 우리 서버의 API를 호출할 수 있는지를 제어하는 설정이다. 이 설정이 `*`(모든 도메인 허용)으로 되어 있으면, 악의적인 외부 사이트에서 우리 API를 자유롭게 호출할 수 있다.

이런 공격 기법을 직접 방어하는 코드를 작성할 필요는 없다. 기능 구현이 완료되면 Claude Code에게 보안 점검을 요청한다:

> 프로젝트 전체를 포괄적으로 보안 점검하고, 문제가 있으면 수정해줘

Claude Code가 코드를 분석하여 취약점을 찾고 수정해 준다. 어떤 문제가 있었는지, 왜 위험한지, 어떻게 수정했는지도 함께 설명해 주므로, 점검 결과를 읽는 것 자체가 보안 공부가 된다. 물론 완벽한 보안은 존재하지 않는다. AI도 모든 취약점을 잡아내지는 못한다. 하지만 흔한 공격 패턴은 상당 부분 방어할 수 있으며, 새로운 기능을 추가할 때마다 이 점검을 반복하면 보안 수준을 꾸준히 높일 수 있다.

## 7.9 정리

- **SvelteKit + Tailwind CSS + PostgreSQL이 이 책의 기본 기술 스택**
  - 기준 버전: SvelteKit 3, Svelte 5(runes), Tailwind CSS 4, Node 24 LTS
  - SvelteKit: 코드량이 적고 파일 기반 라우팅을 지원하는 풀스택 프레임워크. 상태는 `$state`, `$derived`, `$props` 같은 룬으로 다룬다
  - Tailwind CSS: HTML과 스타일이 같은 파일에 있어 AI가 맥락을 파악하기 쉬운 CSS 프레임워크. 설정은 `src/routes/layout.css`에서 한다
  - PostgreSQL: Docker로 간편하게 실행하는 오픈소스 관계형 데이터베이스
- **프로젝트 초기화는 직접 수행하고, 이후 기능 추가는 AI에게 맡기기**
  - `npx sv create`로 뼈대 생성 후 AI와 협업
- **Docker Compose로 개발 환경을 통합 관리**
  - compose.dev.yml(개발용, 5173 포트)과 compose.yml(배포용, 3000 포트)을 분리
  - Dockerfile, compose 파일 생성은 Claude Code에게 요청
- **환경 변수(.env)는 반드시 사용자가 직접 작성**
  - `~/.claude/settings.json`의 `permissions.deny`로 Claude Code가 `.env`를 읽지 못하게 막기
  - 글로벌 CLAUDE.md의 `.env` 접근 금지 규칙은 보조 수단으로 사용
  - `src/env.ts`에 변수를 선언하고 `public: true`로 공개 여부를 구분, `.env`는 `.gitignore`에 포함
- **CLAUDE.md에는 AI가 코드만으로 알 수 없는 정보를 짧게 작성**
  - `/init`으로 초안을 만든 뒤 필요 없는 줄은 지우기
  - 반복되는 실수와 새 규칙을 추가하며 지속적으로 관리
