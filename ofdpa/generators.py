from oftest.testutils import *
from oftest import config
import oftest.base_tests as base_tests
import time

class QinQPacketGenerator( base_tests.DataPlaneOnly ):
    """
    Generator for QinQ packets.
    """
    def runTest( self ):
        # Get the ports and the interfaces
        ports           = config[ "interfaces" ]
        in_port         = ports[0][0]
        in_interface    = ports[0][1].strip()
        out_port        = ports[1][0]
        out_interface   = ports[1][1].strip()
        outer_vlan      = 20
        innner_vlan     = 10
        # Generating the packets
        parsed_pkt = simple_tcp_packet_two_vlan(
            pktlen=108,
            out_dl_vlan_enable=True,
            out_vlan_vid=outer_vlan,
            in_dl_vlan_enable=True,
            in_vlan_vid=innner_vlan
            )
        qinq_pkt = str( parsed_pkt )
        # Sending the packet
        print "\nSending packet on", out_interface
        while True :
            self.dataplane.send( in_port, qinq_pkt )
            time.sleep(1)

class VlanPacketGenerator( base_tests.DataPlaneOnly ):
    """
    Generator for vlan packets.
    """
    def runTest( self ):
        # Get the ports and the interfaces
        ports           = config[ "interfaces" ]
        in_port         = ports[0][0]
        in_interface    = ports[0][1].strip()
        out_port        = ports[1][0]
        out_interface   = ports[1][1].strip()
        outer_vlan      = 20
        # Generating the packets
        parsed_pkt = simple_tcp_packet(
            pktlen=108,
            dl_vlan_enable=True,
            vlan_vid=outer_vlan
            )
        vlan_pkt = str( parsed_pkt )
        # Sending the packet
        print "\nSending packet on", out_interface
        while True :
            self.dataplane.send( in_port, vlan_pkt )
            time.sleep(1)

class UntaggedPacketGenerator( base_tests.DataPlaneOnly ):
    """
    Generator for untagged packets.
    """
    def runTest( self ):
        # Get the ports and the interfaces
        ports           = config[ "interfaces" ]
        in_port         = ports[0][0]
        in_interface    = ports[0][1].strip()
        out_port        = ports[1][0]
        out_interface   = ports[1][1].strip()
        # Generating the packets
        parsed_pkt = simple_tcp_packet(
            pktlen=108,
            )
        untagged_pkt = str( parsed_pkt )
        # Sending the packet
        print "\nSending packet on", out_interface
        while True :
            self.dataplane.send( in_port, untagged_pkt )
            time.sleep(1)
