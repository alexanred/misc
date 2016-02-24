#!/usr/bin/perl
#tcpclient.pl
use threads;
use IO::Socket::INET;

# flush after every write
$| = 1;

sub sentmessage() {
my $cnt = shift;
my ($socket,$client_socket);

# creating object interface of IO::Socket::INET modules which internally creates
# socket, binds and connects to the TCP server running on the specific port.
$socket = new IO::Socket::INET (
PeerHost => '127.0.0.1',
PeerPort => '19999',
Proto => 'tcp',
);

#or die "ERROR in Socket Creation : $!\n";

print "TCP Connection Success.\n";


# write on the socket to server.
$data = "DATA from $$cnt Client \n\r";
print $socket "$data\n";
# we can also send the data through IO::Socket::INET module,
# $socket->send($data);

# read the socket data sent by server.
$data = <$socket>;
# we can also read from socket through recv()  in IO::Socket::INET
# $socket->recv($data,1024);
print "Received from Server : $data\n";

sleep (10);
$socket->close();
}

my $num_threads = 10;
my @Threads;
for ($count = 0; $count < 10; $count++) {
 	print "$count ";
    my $thread = threads->new( \&sentmessage, \$count);
    push (@Threads, $thread);
    my $tid = $thread->tid;
 }
 
 foreach $thr (@Threads) {
 $thr->join();
 }
 
 