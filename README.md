# 개인 프로필 웹사이트

Node.js 기본 모듈만으로 실행하는 정적 웹사이트입니다. 외부 패키지 설치나 `npm install`은 필요하지 않습니다. Node.js 20 이상을 사용하세요.

## 로컬 실행

프로젝트 루트에서 실행합니다.

```powershell
npm start
```

브라우저에서 http://localhost:3000 을 엽니다. 종료는 터미널에서 `Ctrl+C`를 누릅니다. PowerShell 실행 정책으로 `npm`이 차단되면 `npm.cmd start`를 사용하세요.

포트가 이미 사용 중이면 다른 포트를 지정합니다.

```powershell
$env:PORT = '3001'
npm.cmd start
```

이 경우 http://localhost:3001 로 접속합니다. `npm run dev`는 서버 코드가 변경되면 서버를 재시작합니다. HTML, CSS, JavaScript 수정은 브라우저를 새로고침하면 반영됩니다.

## 폴더 구성

```text
public/
  index.html          # 시작 페이지
  styles.css          # 기존 스타일
  script.js           # 기존 동작
scripts/
  server.mjs          # Node.js 로컬 정적 서버
stitch-export/        # 원본 Stitch 디자인
build_profile.py      # 원본으로부터 public/index.html을 재생성하는 기존 도구
package.json          # 실행 명령 (외부 의존성 없음)
vercel.json           # 정적 배포 설정
```

웹사이트 수정은 `public/` 안에서 진행합니다. 이미지 등 공개할 파일도 이 폴더에 추가하세요. 서버는 `public/`만 제공하며 원본 디자인, ZIP, 개발 도구는 공개하지 않습니다. `build_profile.py`를 실행하면 HTML 편집 내용이 덮어써질 수 있습니다. 일반 실행에는 이 도구가 필요하지 않습니다.

## Vercel 정적 배포

저장소를 Vercel에 연결하고 프로젝트 루트를 Root Directory로 선택하세요. 포함된 `vercel.json`은 Framework Preset을 Other, Output Directory를 `public`로 지정하고 설치·빌드 단계를 생략합니다. Node.js 로컬 서버를 배포할 필요 없이 `public/`의 파일만 정적으로 제공합니다. 이번 작업에서는 실제 배포를 수행하지 않았습니다.

공식 설정 문서: https://vercel.com/docs/project-configuration/vercel-json

## 기존 웹사이트 안내

디자인과 웹사이트 파일의 내용은 유지했습니다. 개인정보, 경력, 프로젝트와 수치는 예시이며, 프로젝트 카드는 관련 기술의 공식 사이트로 연결됩니다.

기존 Tailwind CDN, Google Fonts, 외부 프로필 이미지에는 인터넷 연결이 필요합니다. 이메일과 문의 폼은 기기에 설정된 메일 앱을 열며 사이트 자체에서 이메일을 발송하지 않습니다.
