import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from "react-router-dom";
import * as Yup from 'yup';
import logo from '../../assets/images/logo.png';

import {
  USERNAME_REQUIRED,
  PASSWORD_REQUIRED,
  PASSWORD_VALID,
} from '../../constants/errorConstants';

import { loginRequest } from '../../store/actions/';
import { Spinner } from '../../components';

const Login = () => {
  // const [passwordShown, setPasswordShown] = useState(false);
  const [emailValue, setEmailValue] = useState();
  const [passwordValue, setPasswordValue] = useState({});
  const [errValue, setErrValue] = useState();

  const handleValidation = () => {
    let errors = {};
    let formIsValid = true;

    // //Name
    // if (!usernameValue) {
    //   formIsValid = false;
    //   errors = "Username Cannot be empty";
    // }

    //Email
    if (!emailValue) {
      formIsValid = false;
      errors = "Username Cannot be empty";
    }

    // if (emailValue !== "undefined") {
    //   let lastAtPos = emailValue.lastIndexOf('@');
    //   let lastDotPos = emailValue.lastIndexOf('.');

    //   if (!(lastAtPos < lastDotPos && lastAtPos > 0 && emailValue.indexOf('@@') == -1 && lastDotPos > 2 && (emailValue.length - lastDotPos) > 2)) {
    //     formIsValid = false;
    //     errors = "Email is not valid";
    //   }
    // }
    //Password
    if (!passwordValue) {
      formIsValid = false;
      errors = "Password Cannot be empty";
    }

    if (passwordValue && passwordValue.length < 8) {
      formIsValid = false;
      errors = "Password Cannot be less than 8 digits";
    }
    setErrValue(errors);

    return formIsValid;
  }

  const dispatch = useDispatch();

  const submitBtnHandler = () => {
    if (handleValidation()) {
      dispatch(loginRequest({ username: emailValue, password: passwordValue }));
    } else {
      console.log("Error Value", errValue)
    }

  };

  // const togglePasswordVisiblity = () => {
  //   setPasswordShown(passwordShown ? false : true);
  // };
  // const history = useHistory();

  return (
    <div id='main-wrapper'>
      <div className='authincation section-padding'>
        <div className='container h-100'>
          <div className='row justify-content-center h-100 align-items-center'>
            <div className='col-xl-5 col-md-6'>
              <div className='mini-logo text-center my-4'>
                <a href='./intro.html' />
                <img src={logo} alt='' />
                <h4 className='card-title mt-3'>Sign in to Bookstagram</h4>
              </div>
              <div className='auth-form card'>
                <div className='card-body'>
                  <div className='col-12'>
                    <input
                      type='email'
                      className='form-control'
                      placeholder='username'
                      name='email'
                      onChange={(e) => setEmailValue(e.target.value)}
                    />
                  </div>
                  <div className='col-12'>
                    <input
                      type='password'
                      className='form-control'
                      placeholder='Password'
                      name='password'
                      onChange={(e) => setPasswordValue(e.target.value)}
                      required
                    />
                  </div>
                  <div className='col-6'>
                    <div className='form-check form-switch'>
                      <input
                        className='form-check-input'
                        type='checkbox'
                        id='flexSwitchCheckDefault'
                        onChange={(e) => console.log("Hi", e.target.value)}
                      />
                      <label className='form-check-label' htmlFor='flexSwitchCheckDefault'>
                        Remember me
                        </label>
                      {
                        errValue ?
                          <p style={{ color: "red" }}>{errValue}</p>
                          : null
                      }
                    </div>
                  </div>
                  <div className='col-6'>
                    <Link to='/reset-password'>Forgot Password?</Link>
                  </div>
                  <br/>
                  <div className='text-center'>
                    <button
                      type='submit'
                      className='btn btn-primary btn-block'
                      onClick={() => submitBtnHandler()}
                    >
                      Sign in
                      </button>
                  </div>
                  <p className='mt-3 mb-0'>
                    Don't have an account?{' '}
                    <Link
                      className='text-primary'
                      to='/signup'
                    >
                      Sign up
                    </Link>
                  </p>
                </div>
              </div>
              <div className='privacy-link'>
                <Link
                  to='/privacy-policy'>
                  Privacy Policy
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
export default Login;
