"""
Group table test
Verify each group table can created correctly
"""
from oftest import config
import oftest.base_tests as base_tests
import ofp
from oftest.testutils import *
from accton_util import *

class L2InterfaceGroup(base_tests.SimpleDataPlane):
    def runTest(self):    
        delete_all_flows(self.controller)
        delete_all_groups(self.controller)    

        group_list1, msg1 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 1,  False, False)
        group_list2, msg2 =add_l2_interface_grouop(self.controller, config["port_map"].keys(), 2,  False, False)       

        stats = get_stats(self, ofp.message.group_desc_stats_request())
 
        verify_group_stats=[]
        for msg in msg1:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        
        for msg in msg2:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
                                      
        self.assertEquals(stats, verify_group_stats)

        
class L2McastGroup(base_tests.SimpleDataPlane):
    def runTest(self):
        delete_all_flows(self.controller)    
        delete_all_groups(self.controller)    
        
        group_list1, msg1 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 1,  False, False)       
        msg2=add_l2_mcast_group(self.controller, config["port_map"].keys(), 1, 1)
        
        group_list1, msg3 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 2,  False, False)               
        msg4=add_l2_mcast_group(self.controller, config["port_map"].keys(), 2, 2)

        stats = get_stats(self, ofp.message.group_desc_stats_request())
        
        verify_group_stats=[]
        for msg in msg1:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg2.group_type,
                                  group_id=msg2.group_id,
                                  buckets=msg2.buckets)
                                  )
        
        for msg in msg3:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg4.group_type,
                                  group_id=msg4.group_id,
                                  buckets=msg4.buckets)
                                  )

        self.assertEquals(stats, verify_group_stats)


class L2FloodGroup(base_tests.SimpleDataPlane):
    def runTest(self):
        delete_all_flows(self.controller)    
        delete_all_groups(self.controller)    
        
        group_list1, msg1 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 1,  False, False)       
        msg2=add_l2_flood_group(self.controller, config["port_map"].keys(), 1, 1)
        
        group_list1, msg3 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 2,  False, False)               
        msg4=add_l2_flood_group(self.controller, config["port_map"].keys(), 2, 2)

        stats = get_stats(self, ofp.message.group_desc_stats_request())
        
        verify_group_stats=[]
        for msg in msg1:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg2.group_type,
                                  group_id=msg2.group_id,
                                  buckets=msg2.buckets)
                                  )
        
        for msg in msg3:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg4.group_type,
                                  group_id=msg4.group_id,
                                  buckets=msg4.buckets)
                                  )

        self.assertEquals(stats, verify_group_stats)


class L2RewriteGroup(base_tests.SimpleDataPlane):
    def runTest(self):
        delete_all_flows(self.controller)    
        delete_all_groups(self.controller)    
        
        group_list1, msg1 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 1,  False, False)       
        msg2=add_l2_rewrite_group(self.controller, config["port_map"].keys()[0], 1, 1, [00,11,22,33,44,55], [00,22,22,22,22,22])
        
        group_list1, msg3 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 2,  False, False)               
        msg4=add_l2_rewrite_group(self.controller, config["port_map"].keys()[0], 2, 2, [00,11,22,33,44,55], [00,33,33,33,33,33])

        stats = get_stats(self, ofp.message.group_desc_stats_request())
        
        verify_group_stats=[]
        for msg in msg1:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg2.group_type,
                                  group_id=msg2.group_id,
                                  buckets=msg2.buckets)
                                  )
        
        for msg in msg3:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg4.group_type,
                                  group_id=msg4.group_id,
                                  buckets=msg4.buckets)
                                  )

        self.assertEquals(stats, verify_group_stats)
        

class L3UnicastGroup(base_tests.SimpleDataPlane):
    def runTest(self):
        delete_all_flows(self.controller)    
        delete_all_groups(self.controller)    
        
        group_list1, msg1 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 1,  False, False)       
        msg2=add_l3_unicast_group(self.controller, config["port_map"].keys()[0], 1, 1, [0x00,0x11,0x22,0x33,0x44,0x55], [00,0x22,0x22,0x22,0x22,0x22])
        
        group_list1, msg3 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 2,  False, False)               
        msg4=add_l3_unicast_group(self.controller, config["port_map"].keys()[0], 2, 2, [0x00,0x11,0x22,0x33,0x44,0x55], [00,0x33,0x33,0x33,0x33,0x33])

        stats = get_stats(self, ofp.message.group_desc_stats_request())
        
        verify_group_stats=[]
        for msg in msg1:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg2.group_type,
                                  group_id=msg2.group_id,
                                  buckets=msg2.buckets)
                                  )
        
        for msg in msg3:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg4.group_type,
                                  group_id=msg4.group_id,
                                  buckets=msg4.buckets)
                                  )

        self.assertEquals(stats, verify_group_stats)  


class L3ECMPGroup(base_tests.SimpleDataPlane):
    def runTest(self):
        delete_all_flows(self.controller)    
        delete_all_groups(self.controller)    
        
        group_list1, msg1 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 1,  False, False)       
        msg2=add_l3_unicast_group(self.controller, config["port_map"].keys()[0], 1, 1, [0x00,0x11,0x22,0x33,0x44,0x55], [00,0x22,0x22,0x22,0x22,0x22])
        
        group_list1, msg3 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 2,  False, False)               
        msg4=add_l3_unicast_group(self.controller, config["port_map"].keys()[0], 2, 2, [0x00,0x11,0x22,0x33,0x44,0x55], [00,0x33,0x33,0x33,0x33,0x33])

        group_ids=[msg2.group_id, msg4.group_id]
        
        msg5=add_l3_ecmp_group(self.controller, 1, group_ids)
        
        stats = get_stats(self, ofp.message.group_desc_stats_request())

        verify_group_stats=[]
        for msg in msg1:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg2.group_type,
                                  group_id=msg2.group_id,
                                  buckets=msg2.buckets)
                                  )
        
        for msg in msg3:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg4.group_type,
                                  group_id=msg4.group_id,
                                  buckets=msg4.buckets)
                                  )
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg5.group_type,
                                  group_id=msg5.group_id,
                                  buckets=msg5.buckets)
                                  )

        self.assertEquals(stats, verify_group_stats)     


class L3InterfaceGroup(base_tests.SimpleDataPlane):
    def runTest(self):
        delete_all_flows(self.controller)    
        delete_all_groups(self.controller)    
        
        group_list1, msg1 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 1,  False, False)               
        msg2=add_l3_interface_group(self.controller, config["port_map"].keys()[0], 1, 1, [0x00,0x11,0x22,0x33,0x44,0x55])
        group_list1, msg3 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 2,  False, False)                       
        msg4=add_l3_interface_group(self.controller, config["port_map"].keys()[0], 2, 2, [0x00,0x11,0x22,0x33,0x44,0x66])

        stats = get_stats(self, ofp.message.group_desc_stats_request())
        
        verify_group_stats=[]
        for msg in msg1:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg2.group_type,
                                  group_id=msg2.group_id,
                                  buckets=msg2.buckets)
                                  )
        
        for msg in msg3:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg4.group_type,
                                  group_id=msg4.group_id,
                                  buckets=msg4.buckets)
                                  )


        self.assertEquals(stats, verify_group_stats)     


class L3McastGroup(base_tests.SimpleDataPlane):
    def runTest(self):
        delete_all_flows(self.controller)    
        delete_all_groups(self.controller)    

        # Vlan 3 forward to vlan 3 port 1 and 2
        # Vlan 3 foward to vlan 1 port 1
        # Vlan 3 foward to vlan 2 port 1     
        # Vlan 3 foward to vlan 2 port 2             
        group_list1_1, msg1 = add_l2_interface_grouop(self.controller, [config["port_map"].keys()[0]], 1,  False, False)               
        msg2=add_l3_interface_group(self.controller, config["port_map"].keys()[0], 1, 1, [0x00,0x11,0x22,0x33,0x44,0x11])
        group_list1_2, msg3 = add_l2_interface_grouop(self.controller, [config["port_map"].keys()[0]], 2,  False, False)
        msg4=add_l3_interface_group(self.controller, config["port_map"].keys()[0], 2, 2, [0x00,0x11,0x22,0x33,0x44,0x22])
        group_list2_1, msg5 = add_l2_interface_grouop(self.controller, [config["port_map"].keys()[1]], 2,  False, False)
        msg6=add_l3_interface_group(self.controller, config["port_map"].keys()[1], 2, 3, [0x00,0x11,0x22,0x33,0x44,0x33])
        group_list3, msg7 = add_l2_interface_grouop(self.controller, config["port_map"].keys(), 3,  False, False)
        
        group_actions=[msg2.group_id, msg4.group_id, msg6.group_id]
        group_actions.extend(group_list3)

        msg8=add_l3_mcast_group(self.controller, 3, 1, group_actions)
        
        stats = get_stats(self, ofp.message.group_desc_stats_request())
        
        verify_group_stats=[]
        for msg in msg1:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg2.group_type,
                                  group_id=msg2.group_id,
                                  buckets=msg2.buckets)
                                  )
        
        for msg in msg3:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg4.group_type,
                                  group_id=msg4.group_id,
                                  buckets=msg4.buckets)
                                  )
        for msg in msg5:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg6.group_type,
                                  group_id=msg6.group_id,
                                  buckets=msg6.buckets)
                                  )                                      
        for msg in msg7:
            verify_group_stats.append(ofp.group_desc_stats_entry(
                                      group_type=msg.group_type,
                                      group_id=msg.group_id,
                                      buckets=msg.buckets)
                                      )                                      
                                      
        verify_group_stats.append(ofp.group_desc_stats_entry(
                                  group_type=msg8.group_type,
                                  group_id=msg8.group_id,
                                  buckets=msg8.buckets)
                                  )  
                                  
        self.assertEquals(stats, verify_group_stats)     


        