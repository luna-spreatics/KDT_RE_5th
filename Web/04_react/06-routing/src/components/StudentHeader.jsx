import { Link } from 'react-router-dom';

function StudentHeader() {
	const style = {
		display: 'flex',
		gap: '20px',
	};

	return (
		<>
			<h2>ReactRouter 실습</h2>
			<nav>
				<ul style={style}>
					<li>
						<Link to={'/student/kdt'}>학생</Link>
					</li>
					<li>
						<Link to={'/student/codingon'}>코딩온</Link>
					</li>
					<li>
						<Link to={'/student/new?name=re5th'}>searchParams</Link>
					</li>
				</ul>
			</nav>
		</>
	);
}

export default StudentHeader;
