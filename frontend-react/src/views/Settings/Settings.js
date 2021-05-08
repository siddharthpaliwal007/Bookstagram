import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import Sidebar from '../../components/Sidebar/Sidebar';
import Header from '../../components/Header/Header';
//import SettingsHeader from '../../components/SettingsHeader';
import { withRouter } from 'react-router';
import { toast } from 'react-toastify';
import profileImage from '../../assets/images/profile/2.png';

import axiosMain from '../../http/axios/axios_main';
import { date } from 'yup';

const Settings = () => {

    useEffect(async () => {
    });

    const [data, setData] = useState({});
    const [emailValue, setEmailValue] = useState();
    const [dpValue, setDp] = useState();
    const [passwordValue, setPasswordValue] = useState();
    const [usernameValue, setUsernameValue] = useState();
    const [contactValue, setContactValue] = useState();
    const [countryValue, setCountryValue] = useState();
    const [firstnameValue, setFirstnameValue] = useState();
    const [lastnameValue, setLastnameValue] = useState();
    const [usertypeValue, setUsertypeValue] = useState();

    const [errValue, setErrValue] = useState();
    const [updateValue, setUpdateValue] = useState(false);


    useEffect(() => {
        setDp(localStorage.getItem('dp'));
        getUserProfile();
    }, []);

    const getUserProfile = () => {
        const userId = localStorage.getItem('userId');
        console.log("UserId", userId);
        axiosMain
            .get('/user/' + userId + '/')
            .then(response => {
                if (response.status === 200) {
                    console.log("RESPONSE", response)
                    setData(response.data);
                    setUsernameValue(response.data.username);
                    setPasswordValue(response.data.password);
                    setEmailValue(response.data.email);
                    setContactValue(response.data.contact);
                    setFirstnameValue(response.data.first_name);
                    setCountryValue(response.data.country);
                    setLastnameValue(response.data.last_name);
                    setUsertypeValue(response.data.usertype);

                    toast.success(`User Profile Fetch Successful`, {
                        position: 'top-right',
                        autoClose: 3000,
                        hideProgressBar: true,
                        closeOnClick: true,
                        pauseOnHover: true,
                        draggable: true,
                        progress: undefined,
                    });
                }
            })
            .catch(error => {
                setErrValue(error);
                console.error('Error', error);
                setErrValue("This User Profile Fetch Failed")
            });
    };


    const handleUpdate = (e) => {
        e.preventDefault();
        // updateProfileAPI();
        const userId = localStorage.getItem('userId');
        console.log("UserId", userId);
        axiosMain
            .put('/user/' + userId + '/', {
                user: data.user,
                username: usernameValue,
                password: passwordValue,
                country: countryValue,
                email: emailValue,
                contact: contactValue,
                first_name: firstnameValue,
                last_name: lastnameValue,
                usertype: usertypeValue,
                dp: dpValue
            })
            .then(response => {
                if (response.status === 200) {
                    console.log("Response", response)
                    toast.success(`Update Successful`, {
                        position: 'top-right',
                        autoClose: 3000,
                        hideProgressBar: true,
                        closeOnClick: true,
                        pauseOnHover: true,
                        draggable: true,
                        progress: undefined,
                    });
                    console.log("Dp-changes", dpValue);
                    localStorage.setItem('dp', dpValue);
                    setUpdateValue(true);
                    window.location.reload(false);
                }
            })
            .catch(error => {
                console.error('Error', error);
                setErrValue("This Email is already registered on the platform");
            });
    }

    const onImageChange = (event) => {
        if (event.target.files && event.target.files[0]) {
            let reader = new FileReader();
            reader.onload = (e) => {
                setDp(e.target.result);
            };
            reader.readAsDataURL(event.target.files[0]);
        }
    }

    return (
        <React.Fragment>
            <Header />
            <Sidebar />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <div className="content-body">
                <div className="container">
                    <div className="row">
                        <div className="col-xxl-12 col-xl-12">
                            <div className="page-title">
                                <h4>Profile</h4>
                            </div>
                            <div className="card">

                                <div className="card-body">
                                    <div className="row">
                                        <div className="col-xxl-6 col-xl-6 col-lg-6">
                                            <div className="card">
                                                <div className="card-header">
                                                    {updateValue ?
                                                        <h4
                                                            className="card-title"
                                                            style={{ color: "blue" }}>Update Successful</h4>
                                                        :
                                                        null
                                                    }
                                                    <h4 className="card-title">User Profile</h4>
                                                </div>
                                                <div className="card-body">
                                                    <form action="#">
                                                        <div className="row g-3">
                                                            <div className="col-xxl-12">
                                                                <label className="form-label">User Name</label>
                                                                <input
                                                                    type="text" className="form-control" placeholder="username"
                                                                    value={usernameValue}
                                                                    onChange={(e) => { setUsernameValue(e.target.value) }}
                                                                />
                                                            </div>
                                                            <div className="col-xxl-12">
                                                                <div className="d-flex align-items-center">
                                                                    <img className="mr-3 rounded-circle mr-0 mr-sm-3"
                                                                        src={dpValue} width="55" height="55"
                                                                        alt="" />
                                                                    <div className="media-body">
                                                                        <h4 className="mb-0">{usernameValue}</h4>
                                                                        <p className="mb-0">Max file size is 20mb
                                                                    </p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div className="col-xxl-12">
                                                                <div className="form-file">
                                                                    <input
                                                                        type="file"
                                                                        className="form-file-input"
                                                                        id="customFile"
                                                                        onChange={(e) => { onImageChange(e) }}
                                                                    />
                                                                    <label className="form-file-label" for="customFile">
                                                                        <span className="form-file-text">Choose file...</span>
                                                                        <span className="form-file-button">Browse</span>
                                                                    </label>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </form>
                                                </div>
                                            </div>
                                        </div>
                                        <div className="col-xxl-6 col-xl-6 col-lg-6">
                                            <div className="card">
                                                <div className="card-header">
                                                    <h4 className="card-title">User Profile</h4>
                                                </div>
                                                <div className="card-body">
                                                    <form action="#">
                                                        <div className="row g-3">
                                                            <div className="col-xxl-12">
                                                                <label className="form-label">New Email</label>
                                                                <input
                                                                    type="email" className="form-control"
                                                                    placeholder="Email"
                                                                    value={emailValue}
                                                                    onChange={(e) => { setEmailValue(e.target.value) }} />
                                                            </div>
                                                            <div className="col-xxl-12">
                                                                <label className="form-label">New Password</label>
                                                                <input
                                                                    type="password" className="form-control"
                                                                    placeholder="**********"
                                                                    onChange={(e) => { setPasswordValue(e.target.value) }} />
                                                            </div>
                                                        </div>
                                                    </form>
                                                </div>
                                            </div>
                                        </div>
                                        <div className="col-xxl-12">
                                            <div className="card">
                                                <div className="card-header">
                                                    <h4 className="card-title">Personal Information</h4>
                                                </div>
                                                <div className="card-body">
                                                    <form method="post" name="myform" className="personal_validate"
                                                        novalidate="novalidate">
                                                        <div className="row g-4">
                                                            <div className="col-xxl-6 col-xl-6 col-lg-6">
                                                                <label className="form-label">Contact Number</label>
                                                                <input
                                                                    type="text" className="form-control"
                                                                    placeholder="+91" name="contact"
                                                                    value={contactValue}
                                                                    onChange={(e) => { setContactValue(e.target.value) }} />
                                                            </div>
                                                            {/* <div className="col-xxl-6 col-xl-6 col-lg-6">
                                                                <label className="form-label">Email</label>
                                                                <input
                                                                    type="email" className="form-control"
                                                                    placeholder="Hello@example.com"
                                                                    name="email"
                                                                    value={data.email}
                                                                    onChange={(e) => { setData({ "email": e.target.value }) }} />
                                                            </div> */}
                                                            {/* <div className="col-xxl-6 col-xl-6 col-lg-6">
                                                                <label className="form-label">Date of birth</label>
                                                                <input type="text" className="form-control hasDatepicker"
                                                                    placeholder="10-10-2020" id="datepicker"
                                                                    autocomplete="off" name="dob" />
                                                            </div> */}
                                                            <div className="col-xxl-6 col-xl-6 col-lg-6">
                                                                <label className="form-label">First Name</label>
                                                                <input
                                                                    type="text" className="form-control"
                                                                    placeholder="Dishant"
                                                                    name="firstname"
                                                                    value={firstnameValue}
                                                                    onChange={(e) => { setFirstnameValue(e.target.value) }} />
                                                            </div>
                                                            <div className="col-xxl-6 col-xl-6 col-lg-6">
                                                                <label className="form-label">Last Name</label>
                                                                <input
                                                                    type="text" className="form-control"
                                                                    placeholder="Shah"
                                                                    name="lastname"
                                                                    value={lastnameValue}
                                                                    onChange={(e) => { setLastnameValue(e.target.value) }} />
                                                            </div>
                                                            <div className="col-xxl-6 col-xl-6 col-lg-6">
                                                                <label className="form-label">Country</label>
                                                                <input
                                                                    type="text" className="form-control"
                                                                    placeholder="India" name="country"
                                                                    value={countryValue}
                                                                    onChange={(e) => { setCountryValue(e.target.value) }} />
                                                            </div>
                                                            <div className="col-xxl-6 col-xl-6 col-lg-6">
                                                                <label className="form-label">User Type</label>
                                                                <input
                                                                    type="text" className="form-control" name="usertype"
                                                                    value={usertypeValue}
                                                                    onChange={(e) => { setUsertypeValue(e.target.value) }}>

                                                                </input>
                                                            </div>

                                                            <div className="col-12">
                                                                <button
                                                                    className="btn btn-success pl-5 pr-5 waves-effect"
                                                                    onClick={(e) => handleUpdate(e)}
                                                                >
                                                                    Save
                                                                </button>
                                                            </div>
                                                        </div>
                                                    </form>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>


        </React.Fragment>
    );
}

export default Settings;