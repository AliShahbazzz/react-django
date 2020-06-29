import React, { Component } from 'react';
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default class Machine extends Component {
    constructor(props) {
        super(props);
        this.state = {
            values: {
                class: '',
                siblings: '',
                children: '',
                male: '1',
                female: '0'
            },
            final: '',
            message: ''
        }
    }

    updateVal = (field, e) => {
        let val = e.target.value
        let curVal = this.state.values
        curVal[field] = val
        this.setState({
            values: curVal
        })
    }

    updateGender = (e) => {
        let val = e.target.value
        let curVal = this.state.values
        if (val === "male") {
            curVal['male'] = "1"
            curVal['female'] = "0"
            this.setState({ values: curVal })
        }
        else {
            curVal['male'] = "0"
            curVal['female'] = "1"
            this.setState({ values: curVal })
        }
    }

    submit = (e) => {
        e.preventDefault();
        let value = this.state.values;
        return (
            axios.post('ml/learn/', {
                PassengerClass: value.class,
                No_siblings: value.siblings,
                No_children: value.children,
                female: value.female,
                male: value.male,
                result: ''
            })
                .then(res => {
                    console.log(res)
                    if (res.status === 200) {
                        this.setState({
                            final: 'Thank You!'
                        })
                        if (res.data.message === "[1]") {
                            this.setState({ message: 'Alive' })
                        }
                        else {
                            this.setState({ message: 'Dead' })
                        }
                    }
                })
                .catch(err => this.setState({ final: 'Error 404!' }, console.log(err)))
        )
    }
    render() {
        return (
            <div className="form-main">
                TITANIC
                <p>{this.state.final}</p>
                <p>{this.state.message}</p>
                <form onSubmit={this.submit}>
                    <p>Passenger Class:
                    <input type="number" name="class" value={this.state.class} onChange={(e) => this.updateVal('class', e)} />
                    </p><p>Number of Siblings:
                    <input type="number" name="siblings" value={this.state.siblings} onChange={(e) => this.updateVal('siblings', e)} />
                    </p><p>Number of Children:
                    <input type="number" name="children" value={this.state.children} onChange={(e) => this.updateVal('children', e)} />
                    </p>Gender
                    <div onChange={(e) => this.updateGender(e)}>
                        <input type="radio" name="gender" value="male" defaultChecked /><label>Male</label>
                        <input type="radio" name="gender" value="female" /><label>Female</label>
                    </div>
                    <p><button type="submit">Submit</button></p>
                </form>
            </div>
        );
    }
}