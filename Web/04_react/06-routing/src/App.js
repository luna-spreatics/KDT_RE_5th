import { Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import './styles/App.css';

function App() {
	return (
		<div className='App'>
			<Header />
			<Routes>
				<Route path='/' element={<h1>Home</h1>} />
				<Route path='/products' element={<h1>Products Page</h1>} />
				<Route
					path='/products/:productId'
					element={<h1>Product detail Page</h1>}
				/>
			</Routes>
		</div>
	);
}

export default App;
