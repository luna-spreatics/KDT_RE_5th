import './App.css';

function App() {
	const name = 'Luna';
	const styles = {
		backgroundColor: 'yellow',
		color: 'pink',
		fontSize: '48px',
	};

	// 실습
	const name1 = '로이';
	const animal = '강아지';

	const a = 8;
	const b = 5;

	const title = 'Hello World';
	return (
		<>
			<div className='App'>
				{/* JSX 문법 */}
				{/* 1. 하나로 감싸인 요소 */}
				<div>반가워요</div>
				{/*
					2. javascript 표현식 사용
					- {}로 감싸면 js 표현식 사용 가능
					- {} 안에서 삼항 연산자 사용 가능 (if, for 등은 안됨)
				 */}
				<div>{name} 안녕하세요</div>
				<div>{name === 'Luna' ? '반갑습니다' : '누구세요?'}</div>

				{/* 
					3. style 속성
					- 리액트에서 dom 요소에 스타일 적용시 문자열 X -> 객체 사용
					- 스타일 이름 중 하이픈(-) 포함시 camelCase로 작성해야 함
				*/}
				<div style={styles}>하이</div>
				<div
					style={{
						backgroundColor: 'yellow',
						color: 'pink',
						fontSize: '48px',
					}}
				>
					반가워요
				</div>

				{/* 
					4. className 사용
					- class 속성이 아닌 className 속성 사용!

					5. 종료 태그가 없는 태그의 사용
					- 기존의 종료 태그가 없는 태그를 사용하더라도 종료 태그를 작성해야 함 or self-closing

					6. 주석
					- //: jsx 외부 주석
				*/}
			</div>

			{/* 실습 */}
			<div>
				{/* 실습 1번 */}
				<div>
					제 반려 동물의 이름은 <span className='underline'>{name1}</span>
					입니다.
				</div>
				<div>
					<span className='underline'>{name1}</span>는{' '}
					<span className='underline'>{animal}</span>입니다.
				</div>

				{/* 실습 2번 */}
				<div>{3 + 5 === 8 ? '정답입니다!' : '오답입니다!'}</div>

				{/* 실습 3번 */}
				{a > b && 'a가 b보다 큽니다'}

				{/* 실습 4번 */}
				<h1 className='title'>{title}</h1>
				<div style={{ textAlign: 'center' }}>
					<div>
						아이디 : <input type='text' />
					</div>
					<div>
						비밀번호 : <input type='text' />
					</div>
				</div>
			</div>
		</>
	);
}

export default App;
