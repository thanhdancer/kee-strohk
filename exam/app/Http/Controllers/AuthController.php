<?php

namespace App\Http\Controllers;

use App\User;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;

class AuthController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        //
    }

    public function login(Request $request)
    {
        $this->validate($request, [
            'email'    => 'required|email',
            'password' => 'required',
        ]);

        $credentials = $request->only('email', 'password');
        try {
            $user = User::where('email', $request->input('email'))->firstOrFail();
        } catch (ModelNotFoundException $e) {
            return response()->json(['error_code' => 404, 'message' => 'Người dùng không tồn tại'], 404);
        }
        
        if ( !Hash::check( $request->input('password'), $user->password ) ) {
            return response()->json(['error_code' => 403, 'message' => 'Thông tin đăng nhập không chính xác'], 403);
        }
        return response()->json(['error_code' => 0, 'message' => '', 'user' => $user]);
    }
}
