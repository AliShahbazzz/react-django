import React, { Component } from 'react';
import './form.css'
import axios from 'axios';

class Form extends Component {
    state = {
        values: {
            'name': '',
            'email': '',
            'message': '',
            'final': ''
        }
    }

    updateVal = (field, e) => {
        let val = e.target.value;
        let curVal = this.state.values;
        curVal[field] = val;

        this.setState({
            values: curVal
        });
    }

    submit = (e) => {
        e.preventDefault();
        let value = this.state.values;
        return (
            axios.post('contactform/contact/', {
                headers: {
                    'Accept': "application/json, text/plain, */*",
                    'Content-Type': "application/json;charset=utf-8"
                },
                name: value.name,
                email: value.email,
                message: value.message
            })
                .then(res => {
                    if (res.status === 201) {
                        this.setState({
                            final: 'Thank You!',
                            name: '',
                            email: '',
                            message: ''
                        })
                    }
                })
                .catch(err => this.setState({ final: 'Error 404!' }))
        )
    }
    render() {
        return (
            <div className="form-main">
                <form onSubmit={this.submit}>
                    <p>{this.state.final}</p>
                    <p>Name: </p>
                    <input type="text" name="name" value={this.state.name} max='20' onChange={(e) => this.updateVal('name', e)} />
                    <p>Email: </p>
                    <input type="email" name="email" value={this.state.email} onChange={(e) => this.updateVal('email', e)} />
                    <p>Message: </p>
                    <textarea type="text" name="message" value={this.state.message} onChange={(e) => this.updateVal('message', e)} />
                    <p><input type="submit" /></p>
                </form>
            </div>
        );
    }
}

export default Form;