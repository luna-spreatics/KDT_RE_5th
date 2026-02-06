import './App.css';
import CssModule from './components/CssModule';
import Faq from './components/Faq';
import StyledComponent from './components/StyledComponent';
import UseMemoEx1 from './components/UseMemoEx1';

function App() {
	return (
		<div className='App'>
			{/* <UseMemoEx1 />

			<hr />
			<Faq /> */}

			<hr />
			{/* CSS Styling */}
			<CssModule />

			{/* Styled Component */}
			<h2>styled-components</h2>
			<StyledComponent />
		</div>
	);
}

export default App;
