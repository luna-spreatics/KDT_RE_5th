import PropTypes from 'prop-types';

// interface Props {
//   name?: String,
//   age: number
// }

export default function FunctionComponent({ name = '기본 이름', age }) {
	const student = '홍길동';
	// console.log(props.name);

	return (
		<div>
			<h1>Hi {student}!</h1>
			{/* <div>넘겨받은 props {props.name}</div> */}
			<div>넘겨받은 props {name}</div>
		</div>
	);
}

// 리액트 18 version 가능 -> TypeScript
FunctionComponent.propTypes = {
	age: PropTypes.number,
};
