import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import LibraryBooks from '@material-ui/icons/LibraryBooks';
import './Entry.css';

class Entry extends Component {
  render() {
    return (
      <div id="top">
        <div id="container">
          <div id="title" className="animated fadeIn delay-2s">
            Lazy
            <LibraryBooks
              id="icon"
              className="animated infinite bounce delay-1s"
            />
            rEEd
          </div>
          <br />
          <Button
            id="button"
            className="animated bounceIn delay-3s"
            onClick={this.props.nextStage}
          > 
            <div className="animated infinite flash delay-4s">- Start -</div>
          </Button>
        </div>
      </div>
    );
  }
}

export default Entry;
