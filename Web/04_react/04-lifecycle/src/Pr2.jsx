import { useState } from 'react';

function Pr2() {
	const [textColor, changeColor] = useState({ color: 'black', text: '검정색' });

	const handleColor = (color, text) => {
		changeColor({ color, text });
	};
	return (
		<>
			<h4 style={{ color: textColor.color }}>{textColor.text} 글씨</h4>
			<button onClick={(e) => handleColor('red', e.target.innerText)}>
				빨간색
			</button>
			<button onClick={(e) => handleColor('blue', e.target.innerText)}>
				파란색
			</button>
		</>
	);
}

export default Pr2;
