// import React from 'react';

// class Reader extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = { page: 'Fetching' };
//     let temp = 0;
//     setInterval(() => {
//       fetch('/page', {
//         body: JSON.stringify({ test: temp++ }),
//         method: 'POST'
//       })
//         .then(response => response.json())
//         .then(data => {
//           this.setState({ page: data['page'] });
//         });
//     }, 3000);
//   }

//   render() {
//     return (
//       <React.Fragment>
//         <p>{this.state.page}</p>
//       </React.Fragment>
//     );
//   }
// }

// export default Reader;
