<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        factory(App\User::class, 50)->create();
        $user = App\User::find(1)->update([
            'name' => 'thanhvc',
            'email' => 'thanhvc@keystroke.dev',
            'password' => Hash::make('123456'),
        ]);
        $user = App\User::find(2)->update([
            'email' => 'linh@keystroke.dev',
            'password' => Hash::make('123456'),
        ]);
    }
}
