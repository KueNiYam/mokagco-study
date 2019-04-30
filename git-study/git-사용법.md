참고: https://rogerdudler.github.io/git-guide/index.ko.html

## 새로운 저장소 만들기

    git init

## 저장소 받아오기

    git clone 경로
    git clone 사용자명@호스트:경로

## 작업의 흐름
첫번째 나무, 작업 디렉토리(Working directory)
 - 실제 파일들로 이루어져 있다.
 
두번째 나무, 인덱스(Index)
 - 준비 영역(staging aread)의 역할을 한다.
 
마지막 나무, HEAD
 - 최종 확정본(commit)를 나타낸다.

## 추가와 확정(commit)

    git add <파일 이름>
    git add *
    git commit -m "이번 확정본에 대한 설명"

## 변경 내용 발행(push)하기

    git push origin master
    git remote add origin <원격 서버 주소>

## 가지(branch)치기
가지는 안전하게 격리된 상태에서 무언가를 만들 때 사용한다.

	git checkout -b feature_x		# 가지 생성
	git checkout master			# master 가지로 돌아옴
	git brach -d feature_x			# 가지 삭제
	git push origin <가지 이름>		# 새로 만든 가지를 원격 저장소로 전송

새로 만든 가지를 원격 저장소로 전송하기 전까지는 다른 사람들이 접근할 수 없다.

## 갱신과 병합(merge)

	git pull				# 로컬 저장소를 원격 저장소에 맞춰 갱신

이렇게 하면 원격 저장소의 변경 내용이 로컬 작업 디렉토리에 받아지고(fetch), 병합(merge)된다.

	git merge <가지 이름>			# 다른 가지에 있는 변경 내용을 현재 가지에 병합
	git add <파일 이름>
	git diff <원래 가지> <비교 대상 가지> 	# 변경 전 내용 비교

## 꼬리표(tag) 달기
스프트웨어의 새 버전을 발표할 때 마다 꼬리표를 달아놓으면 좋다.

	git tag 1.0.0 1b2e1d63ff

위 명령에서 1b2e1d63ff 부분은 꼬리표가 가리킬 확정본 식별자인데, 확정본 식별자는 아래 명령으로 얻을 수 있다.

	git log

## 로컬 변경 내용 되돌리기

	git checkout -- <파일 이름>

로컬에 있는 모든 변경 내용과 확정본을 포기하려면, 아래 명령으로 원격 저장소의 최신 이력을 가져오고, 로컬 master 가지가 저 이력을 가리키도록 할 수 있다.

	git fetch origin
	git reset --hard origin/master

## 유용한 힌트

git의 내장 GUI

	gitk

콘솔에서 git output을 컬러로 출력하기

	git config color.ui true

이력(log)에서 확정본 1개를 딱 한 줄로만 표시하기

	git config format.pretty oneline

파일을 추가할 때 대화식으로 추가하기

	git add -i
