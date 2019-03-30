import ReactDom from 'react-dom';
import React from 'react';
import Entry from './components/Entry';
import Main from './components/Main';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { stage: 0 };
    this.nextStage = this.nextStage.bind(this);
  }

  nextStage() {
    this.setState({ stage: this.state.stage + 1 });
  }

  render() {
    return React.createElement(App.states[this.state.stage], {
      nextStage: this.nextStage
    });
  }
}

App.states = [Entry, Main];
ReactDom.render(<App />, document.getElementById('root'));
