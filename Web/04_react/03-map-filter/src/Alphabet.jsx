import { useState } from 'react';

function Alphabet() {
	const list = ['a', 'b', 'c', 'd', 'e'];

	const [alphabet, setAlphabet] = useState(['b', 'a', 'n', 'a', 'n', 'a']);
	// input 값을 state 변수로 선언
	const [inputAlpha, setIntputAlpha] = useState('');

	const addAlpha = () => {
		const newAlpha = alphabet.concat(inputAlpha);
		setAlphabet(newAlpha);
		setIntputAlpha('');
	};
	return (
		<>
			{/* <ol>
				{list.map((value, idx) => {
					return <li key={idx}>{value}</li>;
				})}
			</ol> */}

			{/* onChange 이벤트로 값의 변경 감지 -> state 변수값이 변경되게끔 만들기 */}
			<input
				type='text'
				placeholder='알파벳 입력'
				value={inputAlpha}
				onChange={(e) => setIntputAlpha(e.target.value)}
			/>
			<button onClick={addAlpha}>ADD</button>
			<ol>
				{alphabet.map((value, idx) => {
					return <li key={idx}>{value}</li>;
				})}
			</ol>
		</>
	);
}

export default Alphabet;
