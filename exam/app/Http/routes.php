<?php

use App\Assignment;
use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$app->get('/', function () use ($app) {
    return view('index');
});
$app->post('api/v1/login', 'AuthController@login');
$app->get('api/v1/assignments', function () use ($app) {
	return Assignment::with('users')->get();
});
$app->get('api/v1/assignment/{id}', ['middleware' => 'auth', function (Request $request, $id) use ($app) {
	return Assignment::with(['submissions' => function ($query) use ($request) {
		$query->where('user_id', $request->user()->id);
	}])->find($id);
}]);
