import './App.css';
import Button from './Button';
import Counter from './Counter';
import FunctionComponent from './FunctionComponent';

function App() {
	return (
		<div className='App'>
			<FunctionComponent name='로이' age='나이' />
			<FunctionComponent />

			<hr />
			<Button link='https://www.google.com'>Google</Button>

			<hr />
			<h2>useState 활용</h2>
			<Counter />
		</div>
	);
}

export default App;
