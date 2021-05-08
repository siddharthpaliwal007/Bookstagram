/* eslint-disable import/prefer-default-export */
import { put, all, takeEvery } from 'redux-saga/effects';
import axios from 'axios';

// import axiosMain from '../../../http/axios/axios_main';
import { loginRequestSuccess, showLoader, hideLoader, loginRequestFail } from '../../actions';
import * as actionLabels from '../../actionLabels';
import { toast } from 'react-toastify';

// eslint-disable-next-line no-unused-vars
function* loginRequestSaga({ payload }) {
  try {
    const { username, password } = payload;
    yield put(showLoader());
    console.log("Response:", payload);

    var bodyFormData = new FormData();
    bodyFormData.append('username', username);
    bodyFormData.append('password', password);

    const axiosMain = axios.create({
      baseURL: 'http://40.80.95.65/store',
      headers: {
      },
    });

    const config = {
      headers: { 'content-type': 'multipart/form-data' }
    }


    let response = yield axiosMain.post('/book/login/', bodyFormData, config);
    if (response.status === 200) {
      console.log("RESPONSE:", response.data);
      // toast.success(`${response.message}`, {
      //   position: 'top-right',
      //   autoClose: 1000,
      //   hideProgressBar: true,
      //   closeOnClick: true,
      //   pauseOnHover: true,
      //   draggable: true,
      //   progress: undefined,
      // });
      yield localStorage.setItem('userToken', response.data.auth_token.token);
      yield localStorage.setItem('userId', JSON.stringify(response.data.app_userid));
      yield localStorage.setItem('userType', response.data.usertype);
      yield localStorage.setItem('dp', response.data.dp);
      yield localStorage.setItem('email', response.data.email);
      yield localStorage.setItem('name', response.data.username);

      yield put(loginRequestSuccess({ userToken: response.data.accessToken, userData: response.data.role }));
      yield put(hideLoader());
      window.location.reload(false);
    } else {
      toast.error(`${response.msg}`, {
        position: 'top-right',
        autoClose: 1000,
        hideProgressBar: true,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
      yield put(loginRequestFail());
      yield put(hideLoader());
    }
  } catch (error) {
    console.log("error", error)
    toast.error(`Something went wrong`, {
      position: 'top-right',
      autoClose: 1000,
      hideProgressBar: true,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
    yield put(hideLoader());
    yield put(loginRequestFail());
  }
}

export default function* rootsaga() {
  yield all([
    yield takeEvery(actionLabels.LOGIN_REQUEST, loginRequestSaga),
  ]);
}