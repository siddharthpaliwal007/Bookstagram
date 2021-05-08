import React, { useState, useEffect } from 'react';
import { Link, useHistory } from 'react-router-dom';
import { withRouter } from 'react-router';
import axios from 'axios';

const VerifyEmail = props => {
    const [emailValue, setEmailValue] = useState();
    const history = useHistory();

    useEffect(() => {
        console.log("Props", props);
        if (!emailValue) {
        if (props.location.state) {

                const axiosMain = axios.create({
                baseURL: 'http://40.80.95.65/store',
                headers: {
                },
                });
                axiosMain
                .post('/create_user/', {
                    first_name: "set name",
                    last_name: "set last name",
                    country: "set country",
                    username: props.location.state.username,
                    email: props.location.state.email,
                    password: props.location.state.password,
                    usertype: props.location.state.usertype
                })
                .then(response => {
                    if (response.status === 200) {
                        setEmailValue(props.location.state.email);

                    console.log("RESPONSE", response);
                    } else {
                        history.push('/login');
                    }
      })
      .catch(error => {
        console.error('Error', error);
      })
        }
         }
        }, []);
    return (
        <div id="main-wrapper">
            <div className="verification section-padding">
                <div className="container h-100">
                    <div className="row justify-content-center h-100 align-items-center">
                        <div className="col-xl-5 col-md-6">
                            <div className="mini-logo text-center my-4">
                                <a href="./intro.html"><img src="./images/logo.png" alt="" /></a>
                                <h4 className="card-title mt-3">Verify your Email</h4>
                            </div>
                            <div className="auth-form card">
                                <div className="card-body">
                                    <form action="verify-step-2.html" className="identity-upload">
                                        { emailValue &&
                                        <div className="identity-content">
                                            <span className="icon"><i className="icofont-email"></i></span>
                                            <p>We sent verification email to <strong
                                                className="text-dark">{emailValue}</strong>. Click the link inside to
                                            get started!</p>
                                            <Link
                                                to="/"
                                            >
                                                Login
                                            </Link>
                                        </div>
                                        }
                                    </form>
                                </div>
                                <div className="card-footer text-center">
                                    <Link
                                        to="signup"
                                    >
                                        Email didn't arrive?
                                    </Link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default withRouter(VerifyEmail);
