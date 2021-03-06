import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

function Square(props) {
    return (
        <button
            className="square"
            onClick={() => props.onClick()}
        >
            {props.value === 0 ? " " : props.value}
        </button>
    );
}


class Board extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            squares: Array(9).fill(null),
            blank: null
        };
    }

    componentDidMount() {
        fetch('/solution').then(res => res.json()).then(data => {
            this.setState({
                squares: data,
                blank: data.indexOf(0)
            });
        });
    }

    handleClick(i) {
        const blank = this.state.blank;
        const diff = i - blank;

        if ( [1, 3].includes(Math.abs(diff))) {
            const squares = this.state.squares.slice();
            squares[i] = 0;
            squares[this.state.blank] = this.state.squares[i]

            this.setState({ squares: squares, blank: i });
        }

    }
        getSolution() {

        fetch('/solution?initial_state=' + (this.state.squares).toString()).then(res => res.json()).then(data => {

            this.setState({

                solution: data

            });

            console.log(data)

            alert('Done')

        });

    }

    handleNew() {
        fetch('/solution').then(res => res.json()).then(data => {
            this.setState({
                squares: data,
                blank: data.indexOf(0)
            });
        });
    }

    renderSquare(i) {
        return (
            <Square
                value={this.state.squares[i]}
                onClick={() => this.handleClick(i)}
            />
        );
    }

    render() {
       
        return (
            <div>
                <button className='tool' onClick={() => this.handleNew()}>New Game</button>
                <div className="board-row">
                    {this.renderSquare(0)}
                    {this.renderSquare(1)}
                    {this.renderSquare(2)}
                </div>
                <div className="board-row">
                    {this.renderSquare(3)}
                    {this.renderSquare(4)}
                    {this.renderSquare(5)}
                </div>
                <div className="board-row">
                    {this.renderSquare(6)}
                    {this.renderSquare(7)}
                    {this.renderSquare(8)}
                </div>
            </div>
        );
    }
}

class Game extends React.Component {
    render() {
        return (
            <div className="game">
                <div className="game-board">
                    <Board />
                </div>
                <div className="game-info">
                    <div>{/* status */}</div>
                    <ol>{/* TODO */}</ol>
                </div>
            </div>
        );
    } 
}

// ========================================

ReactDOM.render(
    <Game />,
    document.getElementById('root')
);
