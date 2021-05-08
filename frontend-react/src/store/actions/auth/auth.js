import * as actionLabels from '../../actionLabels';

export const loginRequest = (payload) => ({
  type: actionLabels.LOGIN_REQUEST,
  payload
});

export const loginRequestSuccess = (payload) => ({
  type: actionLabels.LOGIN_REQUEST_SUCCESS,
  payload
});

export const loginRequestFail = () => ({
  type: actionLabels.LOGIN_REQUEST_FAIL
});
export const onLogout = () => ({
  type: actionLabels.DESTROY_SESSION
});

