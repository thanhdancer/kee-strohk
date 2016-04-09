<?php

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
$app->group(['prefix' => 'api/v1', 'middleware' => 'cors'], function () use ($app) {
	$app->group(['middleware' => 'auth'], function () use ($app) {
	    $app->get('/me', function (Request $request) use ($app) {
	    	return $request->user();
	    });
	});
	$app->post('/login', 'App\Http\Controllers\AuthController@login');
});